#functions
def say_hello():
    """A function that says hello"""
    print("Hello!") 
say_hello()

def say_hello2(username):
    print(f"Hello {username}")
say_hello2("Rabea")


#username = input("enter username")
#language = input("enter lang")
def say_hello(username, language):
    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)
say_hello(username ="Rabea", language = "EN") 