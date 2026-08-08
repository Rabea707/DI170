import random

def compare_numbers(my_number):
    random_number = random.randint(1, 100)
    if my_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {my_number}, Random number: {random_number}")

compare_numbers(50)