// Exercise 3 : Playing with numbers
// Instructions
let age = [20,5,12,43,98,55];
// Requirements : Don’t use built-in Javascript methods to answer the following questions. You have to create the logic by yourself. Use simple for loops.
sum = 0;
for (let i = 0 ; i < age.length; i++){
    sum += age[i];
}
console.log(sum);
// 2. Console.log the highest age in the array.
let highest = age[0];
for (let i = 1; i < age.length; i++){
    if (age[i] > highest){
        highest = age[i];
    }
}
console.log(highest);