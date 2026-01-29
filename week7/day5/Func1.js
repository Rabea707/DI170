function sayhi(name) {
    return `Hello, ${name}!`;
}
sayhi("Alice");

function myage(age){
 const mom = age * 2;
 const dad = mom * 1.2;
}

// 1. Create a structured HTML file linked to a JS file

// 2. Write a Javascript function that takes a parameter: myAge

// 3. In the function, console.log the age of my mum and my dad. My mum is twice my age, and my dad is 1.2 the age of my mum.

// 4. Call the function.
function myage(age){
    const mom = age * 2;
    const dad = mom * 1.2;
    console.log(`My mum is ${mom} years old.`);
    console.log(`My dad is ${dad} years old.`);
}

myage(25);