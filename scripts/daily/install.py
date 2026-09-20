"""Install the reviewed controller as one macOS launch agent."""

import os
import plistlib
import shutil
import subprocess
import sys
from pathlib import Path

LABEL = 'com.karthik.awesome-ai-roadmaps-daily'


def main():
    if sys.platform != 'darwin':
        raise SystemExit('This installer is for macOS launchd.')
    repo = Path(__file__).resolve().parents[2]
    domain = f'gui/{os.getuid()}'
    existing = subprocess.run(['launchctl', 'print', f'{domain}/{LABEL}'], capture_output=True)
    if existing.returncode == 0:
        raise SystemExit('Schedule already registered. Pause it before reinstalling the controller.')
    state = Path.home() / 'Library/Application Support/awesome-ai-roadmaps-daily'
    installed = state / 'controller'
    installed.mkdir(parents=True, exist_ok=True)
    state.chmod(0o700)
    for name in ('run.py', 'audit.py', 'prompt.md'):
        shutil.copyfile(Path(__file__).with_name(name), installed / name)
    agents = Path.home() / 'Library/LaunchAgents'
    agents.mkdir(parents=True, exist_ok=True)
    plist = agents / f'{LABEL}.plist'
    config = {
        'Label': LABEL,
        'ProgramArguments': [sys.executable, str(installed / 'run.py'), '--repo', str(repo), '--state-dir', str(state)],
        'WorkingDirectory': str(repo),
        'EnvironmentVariables': {
            'PATH': '/opt/homebrew/opt/ruby/bin:/opt/homebrew/lib/ruby/gems/4.0.0/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin',
            'TZ': 'Europe/London',
            'PYTHONUNBUFFERED': '1',
        },
        'StartCalendarInterval': {'Hour': 18, 'Minute': 45},
        'RunAtLoad': True,
        'KeepAlive': False,
        'ProcessType': 'Background',
        'LowPriorityIO': True,
        'StandardOutPath': str(state / 'launchd.log'),
        'StandardErrorPath': str(state / 'launchd-error.log'),
    }
    with plist.open('wb') as output:
        plistlib.dump(config, output)
    subprocess.run(['plutil', '-lint', str(plist)], check=True)
    subprocess.run(['launchctl', 'bootstrap', domain, str(plist)], check=True)
    subprocess.run(['launchctl', 'print', f'{domain}/{LABEL}'], check=True)
    print(f'Installed one daily schedule at 18:45 Europe/London. Reports: {state}')


if __name__ == '__main__':
    main()
