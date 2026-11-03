(() => {
  const read = slug => {
    try { return new Set(JSON.parse(localStorage.getItem('progress:' + slug) || '[]')); } catch { return new Set(); }
  };
  const write = (slug, done) => {
    try { localStorage.setItem('progress:' + slug, JSON.stringify([...done])); } catch { /* private mode */ }
  };
  const paint = (root, done, total) => {
    const bar = root.querySelector('.progress span');
    const label = root.querySelector('.progress-label');
    if (bar) bar.style.width = (100 * done / total) + '%';
    if (!label) return;
    if (done === total) label.textContent = 'Completed 🎉';
    else if (done || root.classList.contains('rm-hero')) label.textContent = `${done} of ${total} done`;
    else label.textContent = '';
  };

  // Theme toggle: cycles to the opposite of what is showing now.
  const toggle = document.querySelector('.theme-toggle');
  toggle?.addEventListener('click', () => {
    const root = document.documentElement;
    const dark = root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
    root.dataset.theme = dark ? 'light' : 'dark';
    try { localStorage.setItem('theme', root.dataset.theme); } catch { /* ignore */ }
  });

  // Home: progress per card and search.
  document.querySelectorAll('.card').forEach(card => {
    paint(card, read(card.dataset.slug).size, Number(card.dataset.total));
  });
  const search = document.getElementById('search');
  if (search) {
    const cards = [...document.querySelectorAll('.card')];
    const empty = document.getElementById('empty');
    search.addEventListener('input', () => {
      const terms = search.value.toLowerCase().split(/\s+/).filter(Boolean);
      let shown = 0;
      cards.forEach(card => {
        const hit = terms.every(t => card.dataset.search.includes(t));
        card.hidden = !hit;
        shown += hit;
      });
      empty.hidden = shown > 0;
    });
  }

  // Roadmap page: checkboxes.
  const page = document.querySelector('.roadmap');
  if (!page) return;
  const slug = page.dataset.slug;
  const total = Number(page.dataset.total);
  const hero = page.querySelector('.rm-hero');
  const done = read(slug);
  const boxes = [...page.querySelectorAll('.done input')];
  const next = page.querySelector('.continue');
  const sync = () => {
    boxes.forEach(box => {
      box.checked = done.has(box.dataset.id);
      box.closest('.step').classList.toggle('is-done', box.checked);
    });
    const count = boxes.filter(b => b.checked).length;
    paint(hero, count, total);
    const first = boxes.findIndex(b => !b.checked);
    if (next) {
      next.hidden = !count || first < 0;
      if (first >= 0) {
        next.href = '#step-' + (first + 1);
        next.textContent = `Continue with step ${first + 1} →`;
      }
    }
  };
  boxes.forEach(box => box.addEventListener('change', () => {
    box.checked ? done.add(box.dataset.id) : done.delete(box.dataset.id);
    write(slug, done);
    sync();
  }));
  page.querySelector('.reset')?.addEventListener('click', () => {
    done.clear();
    write(slug, done);
    sync();
  });
  sync();
})();
