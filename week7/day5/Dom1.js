// For each of the questions, find 2 WAYS of accessing :

// 1. The div DOM node?
 const divdom = document.body.firstElementChild;
    
 const divdom2 = document.body.children[0];
 console.log(divdom);
 console.log(divdom2);
// 2. The ul DOM node?
const uldom = document.body.firstElementChild.nextElementSibling

const uldom2 = document.body.children[1];
console.log(uldom);
console.log(uldom2);
// 3. The second li (with Pete)?
const liptedom = document.body.firstElementChild.nextElementSibling.lastElementChild;

const liptedom2 = document.body.children[1].children[1];

const liptedom3 = divdom.nextElementSibling.lastElementChild;

console.log(liptedom);
console.log(liptedom2);
console.log(liptedom3);
