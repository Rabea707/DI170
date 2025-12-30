#Passing list as function arguments

def greeting_user(users):
    for user in users:
        print("Hello " + user.title() + "!")
username = ["Rabea","Mouse","Rami"]
greeting_user(username)

