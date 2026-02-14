const h1 = document.querySelector('h1');
console.log(h1);
console.log(h1.textContent);

const articale = document.querySelector('article');
const p = articale.querySelectorAll('p');
articale.removeChild(p[p.length - 1]);

const button = document.querySelector('#btn1');
button.addEventListener('click', () => {
  articale.style.backgroundColor = 'blue';
});
const h2 = document.querySelector('h2');
h2.addEventListener('click', () => {
  h2.style.backgroundColor = 'red';
});