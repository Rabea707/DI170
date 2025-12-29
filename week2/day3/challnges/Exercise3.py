#Instructions
#Write a script that calculates the number of upper case letters 
#and lower case letters in a string.

upper_count = 0
lower_count = 0

word = input("Enter your word: ")

for char in word:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count +=1
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
