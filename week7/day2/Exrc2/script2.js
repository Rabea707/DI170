// Exercise 2 : Attendance
// Instructions
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}


// Given the object above where the key is the student’s name and the value is the country they are from.

// Prompt the student for their name.
let studentName = prompt("Please enter your name:");

// If the name is in the object, console.log the name of the student and the country they come from.
// For example: "Hi! I'm [name], and I'm from [country]."
// Hint: You don’t need to use a for loop, just look up the statement if ... in
if (studentName in guestList) {
    console.log(`Hi! I'm ${studentName}, and I'm from ${guestList[studentName]}.`);
}

// If the name is not in the object, console.log: "Hi! I'm a guest."
if (!(studentName in guestList)) {
    console.log("Hi! I'm a guest.");
}
