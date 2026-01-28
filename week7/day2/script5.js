// Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.
const family = {
    father: "Jon",
    mother: "Dana",
    son: "Mike",
    daughter: "Sophie"
}
for (let key in family) {
    console.log(key);
}
// for (let i = 0; i < Object.keys(family).length; i++) {
//     console.log(Object.keys(family)[i]);
// }
// both for loops works to log the keys of the object

// for (let value in family) {
//     console.log(family[value]);
// }
console.log("----values----");
for (let i = 0; i < Object.values(family).length; i++) {
    console.log(Object.values(family)[i]);
}
// both for loops works to log the values of the object