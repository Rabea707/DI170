const people = ["Greg", "Mary", "Devon", "James"];
//Write code to remove “Greg” from the people array.
console.log(people)
people.splice(0,1)
console.log(people)
//Write code to replace “James” to “Jason”.
people.splice(3,1,"jason");
console.log(people)
//Write code to add your name to the end of the people array.
people.push("Rabea")
console.log(people)
//Write code that console.logs Mary’s index
console.log(people[0])
//Write code to make a copy of the people array using the slice method.
//The copy should NOT include “Mary” or your name.
//Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
//Hint: Check out the documentation for the slice method
const NewPeople = people.slice(1,3)
console.log(NewPeople)
//Write code that gives the index of “Foo”. Why does it return -1 ?
console.log(people.indexOf("Foo")) // cuz Foo is not in the array
//Create a variable called last which value is the last element of the array.
//Hint: What is the relationship between the index of the last element in the array and the length of the array?

//const last = people.pop()
//console.log(last)

// or we can do it that way
const last = people[people.length - 1]
console.log(last)
//Using a loop, iterate through the people array and console.log each person.
for (let i = 0;i < people.length;i++)
    {
        console.log(people[i])
}
console.log("      ")
//Using a loop, iterate through the people array and exit the loop after you console.log “Devon” .
//Hint: take a look at the break statement in the lesson.
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);

  if (people[i] === "Devon") {
    break;
  }
}