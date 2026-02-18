
/* Robo-Friends: render robots list and enable search with debounce + highlight */

const robots = [
  { id: 1, name: 'Leanne Graham', email: 'Sincere@april.biz', image: 'https://robohash.org/1?200x200' },
  { id: 2, name: 'Ervin Howell', email: 'Shanna@melissa.tv', image: 'https://robohash.org/2?200x200' },
  { id: 3, name: 'Clementine Bauch', email: 'Nathan@yesenia.net', image: 'https://robohash.org/3?200x200' },
  { id: 4, name: 'Patricia Lebsack', email: 'Julianne.OConner@kory.org', image: 'https://robohash.org/4?200x200' },
  { id: 5, name: 'Chelsey Dietrich', email: 'Lucio_Hettinger@annie.ca', image: 'https://robohash.org/5?200x200' },
  { id: 6, name: 'Mrs. Dennis Schulist', email: 'Karley_Dach@jasper.info', image: 'https://robohash.org/6?200x200' },
  { id: 7, name: 'Kurtis Weissnat', email: 'Telly.Hoeger@billy.biz', image: 'https://robohash.org/7?200x200' },
  { id: 8, name: 'Nicholas Runolfsdottir V', email: 'Sherwood@rosamond.me', image: 'https://robohash.org/8?200x200' },
  { id: 9, name: 'Glenna Reichert', email: 'Chaim_McDermott@dana.io', image: 'https://robohash.org/9?200x200' },
  { id: 10, name: 'Clementina DuBuque', email: 'Rey.Padberg@karina.biz', image: 'https://robohash.org/10?200x200' }
];

document.addEventListener('DOMContentLoaded', () => {
  const $cards = document.getElementById('cards');
  const $search = document.getElementById('search');
  const $noResults = document.getElementById('no-results');

  function escapeHtml(s){
    return String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'})[c]);
  }

  function highlight(text, query){
    if(!query) return escapeHtml(text);
    const safe = query.replace(/[.*+?^${}()|[\\]\\]/g,'\\$&');
    const re = new RegExp(`(${safe})`,'ig');
    return escapeHtml(text).replace(re, '<span class="highlight">$1</span>');
  }

  function render(list, q){
    $cards.innerHTML = '';
    if(!list || list.length === 0){
      $noResults.hidden = false;
      return;
    }
    $noResults.hidden = true;
    const frag = document.createDocumentFragment();
    list.forEach(r => {
      const el = document.createElement('article');
      el.className = 'card';
      const img = r.image || `https://robohash.org/${encodeURIComponent(r.id)}?size=200x200`;
      el.innerHTML = `\n      <img class="avatar" src="${img}" alt="Robot avatar for ${escapeHtml(r.name)}">\n      <div class="name">${highlight(r.name, q)}</div>\n      <div class="email">${highlight(r.email, q)}</div>\n      <div class="id">#${r.id}</div>\n    `;
      frag.appendChild(el);
    });
    $cards.appendChild(frag);
  }

  function filterRobots(q){
    const t = String(q || '').trim().toLowerCase();
    if(!t) return robots;
    return robots.filter(r => r.name.toLowerCase().includes(t) || r.email.toLowerCase().includes(t));
  }

  function debounce(fn, wait = 150){
    let id = null;
    return (...args) => { clearTimeout(id); id = setTimeout(() => fn(...args), wait); };
  }

  const onSearch = debounce(() => {
    const q = $search.value || '';
    const filtered = filterRobots(q);
    render(filtered, q);
  }, 160);

              $search.addEventListener('input', onSearch);

              // initial render
              render(robots, '');
            })
    
