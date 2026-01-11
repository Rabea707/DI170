favorite_fruits = input("Enter your favorite fruits (separated by spaces): ")
favorite_fruits = favorite_fruits.split()

fruit = input("Enter a fruit: ")

if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
