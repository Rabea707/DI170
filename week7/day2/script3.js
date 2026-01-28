// Exercise 3 : Repeat the question

// Prompt the user for a number
let num = prompt("Enter a number");

// Check the data type
console.log(typeof num); // string

// Convert to number
num = Number(num);

// While the number is smaller than 10, keep asking
while (isNaN(num) || num < 10) {
  num = prompt("Number is too small or invalid. Enter a number 10 or higher:");
  console.log(typeof num); // string

  num = Number(num);
}

// Final message
console.log("Thank you! The number is " + num);
