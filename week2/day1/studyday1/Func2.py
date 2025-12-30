# Local and Global scope
my_number = 5
def numberator(number):
    new_number = number * my_number
    print(f"{my_number} times {number} is {new_number}")
numberator(10)

#Return vaules
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)

#more examples
def divide_by_three(number):
  return number / 3

first_number = 12
first_number_computed = divide_by_three(first_number)   
print(first_number_computed)


second_number = 27
second_number_computed = divide_by_three(second_number)
print(second_number_computed)

#Returing with tuple 
my_tuple = ("jimi", "hendrix")
first_name, last_name = my_tuple
print("First name is: " + first_name)
print("Last name is: " + last_name)

def format_name(first_name, last_name):
    return (first_name.title(), last_name.title())

first, last = format_name("RICk", "mORTY")
print(first)
print(last)
print(first , last , end="")