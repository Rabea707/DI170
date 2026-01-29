// Exercise 2 : Shopping List
// Instructions
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
// Add the stock and prices objects to your js file.

// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.
const shoppingList = ["banana", "orange", "apple"];

// Create a function called myBill() that takes no parameters.
    function myBill() {
        let totalPrice = 0;
        for (let i = 0; i < shoppingList.length; i++) {
            let item = shoppingList[i];
            if (item in stock && stock[item] > 0) {
                totalPrice += prices[item];
                // Bonus: If the item is in stock, decrease the item’s stock by 1
                stock[item] -= 1;
            }
        }
        return totalPrice;
    }

// In the function, loop through the shoppingList array.
    
// For each item, check if it is in stock. If the item is in stock, add the price to the total price.                                                           
// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.

// Call the myBill() function.
console.log("Total Price:", myBill());

// Bonus: If the item is in stock, decrease the item’s stock by 1
console.log("Updated Stock:", stock);