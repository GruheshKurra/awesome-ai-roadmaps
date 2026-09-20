"""Bounded availability checks. HTTP success is not proof of free access or quality."""

import concurrent.futures
import ipaddress
import json
import re
import socket
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

USER_AGENT = 'AwesomeAIRoadmaps-LinkCheck/1.0 (+https://github.com/GruheshKurra/awesome-ai-roadmaps)'


def resource_links(root):
    links = {}
    for path in sorted((Path(root) / 'tracks').glob('*/README.md')):
        for line in path.read_text().splitlines():
            if not re.match(r'^\|\s*\d+\s*\|', line):
                continue
            for url in re.findall(r'\]\((https?://[^\s)]+)\)', line):
                links.setdefault(url, []).append(str(path.relative_to(root)))
    return links


def public_url(url):
    """Do not let resource URLs or redirects probe the machine's private network."""
    parsed = urlsplit(url)
    if parsed.scheme not in ('http', 'https') or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError('Expected a public HTTP(S) URL without credentials')
    if parsed.port not in (None, 80, 443):
        raise ValueError('Unexpected resource port')
    addresses = socket.getaddrinfo(parsed.hostname, parsed.port or 443, type=socket.SOCK_STREAM)
    if not addresses or any(not ipaddress.ip_address(item[4][0]).is_global for item in addresses):
        raise ValueError('Private or reserved destination')
    return url


class PublicRedirect(HTTPRedirectHandler):
    # Python 3.9's standard handler predates support for permanent 308 redirects.
    http_error_308 = HTTPRedirectHandler.http_error_302

    def redirect_request(self, request, fp, code, msg, headers, newurl):
        public_url(newurl)
        return super().redirect_request(request, fp, 307 if code == 308 else code, msg, headers, newurl)


def probe(url, timeout=12):
    request_url = url
    parsed = urlsplit(url)
    youtube = parsed.hostname in ('youtube.com', 'www.youtube.com', 'm.youtube.com')
    if youtube:
        request_url = 'https://www.youtube.com/oembed?' + urlencode({'url': url, 'format': 'json'})
    last = None
    for attempt in range(2):
        try:
            public_url(request_url)
            request = Request(request_url, headers={'User-Agent': USER_AGENT})
            with build_opener(PublicRedirect()).open(request, timeout=timeout) as response:
                result = {'status': 'reachable', 'http_status': response.status,
                          'final_url': response.geturl(), 'method': 'youtube-oembed' if youtube else 'get'}
                if youtube:
                    metadata = json.loads(response.read(65536))
                    result['title'] = metadata.get('title', '')
                # Stop after headers for large PDFs; do not download the resource body.
                return result
        except HTTPError as error:
            last = {'status': 'unavailable' if error.code in (404, 410) else 'uncertain',
                    'http_status': error.code, 'detail': 'HTTP response requires review'}
            error.close()
            if error.code not in (408, 429, 500, 502, 503, 504):
                break
        except (URLError, TimeoutError, OSError, ValueError) as error:
            last = {'status': 'uncertain', 'detail': type(error).__name__}
        if attempt == 0:
            time.sleep(1)
    return last


def audit(root, previous=None, urls=None, workers=4):
    links = resource_links(root)
    selected = sorted(links if urls is None else set(urls))
    previous = previous or {}
    today = datetime.now(timezone.utc).date().isoformat()
    output = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(probe, url): url for url in selected}
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            result = future.result()
            before = previous.get(url, {})
            unavailable = result['status'] == 'unavailable'
            streak = before.get('unavailable_days', 0)
            if not unavailable:
                streak = 0
            elif before.get('checked_date') != today:
                streak += 1
            elif streak == 0:
                streak = 1
            result.update(checked_date=today, unavailable_days=streak, tracks=links.get(url, []))
            output[url] = result
    return dict(sorted(output.items()))
