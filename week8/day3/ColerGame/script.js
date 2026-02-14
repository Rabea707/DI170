const myArray = [2, 3, 4, 5, 6]; 

//1st example with arrow function
myArray.forEach((number, index) => { 
    console.log("number: ", number) // logs each element of the array
    console.log("index: ", index) // logs each index of the array
}); 
const obj1 = { 
    city: "New York",
    country: "USA",
    getLocation: function() {
        console.log(this.city + ", " + this.country); // logs "New York, USA"
    }
};
obj1.getLocation();

//2nd example with arrow function
const obj2 = { 
    city: "Los Angeles",
    country: "USA",
    getLocation: () => {
        console.log(this.city + ", " + this.country); // logs "undefined, undefined" because arrow functions do not have their own 'this' context
    }
};
obj2.getLocation(); 
