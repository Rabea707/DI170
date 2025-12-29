#Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

def is_short(name):
    return len(name) <= 4

def say_hello(name):
    return "Hello " + name

short_names = filter(is_short, people)
greetings = map(say_hello, short_names)

for greeting in greetings:
    print(greeting)
