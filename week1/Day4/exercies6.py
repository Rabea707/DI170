
while True:
    user_name = input("Enter your name")
    if len(user_name) < 3 or user_name.isdigit():
        print("name must be longer than 2 and doesnt have number")
    else :
        print("thank you")
        break
print(user_name)