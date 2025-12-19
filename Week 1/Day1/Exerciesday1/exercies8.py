#Ask the user for a number between 1 and 100
#If the number is a divisible by three, print Fizz
#If the number is a divisible by five, print Buzz.
#If the number is a divisible by both three and five, print FizzBuzz instead.

number = int(input("enter a number bteween 1 and 100"))

if number % 3 ==0 :
    print("fizz")
elif number % 5 == 0:
    print("buzz")
elif number % 3 == 0 and number % 5 ==0:
    print("fizzbuzz")