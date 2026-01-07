year = 2025
my_list = ['car', 16, 42 , year]
print(my_list[0], my_list[1], my_list[3])
print(my_list[-1]) #Negative indux starts from the last indux to the first so thsis prints year
print(my_list[0:2]) # this gives a range from where you wanna start to end it but going up to 1 but not inclduing 2
#####################################################################################################################
my_hobbies = ["code","netflix","chill",67]
my_hobbies[3] = 69 # this Modify the list
print(my_hobbies)

my_hobbies.append("Rabea") # .append adds elemnt in the list
print(my_hobbies)

my_hobbies.remove("Rabea") # this removes elemnt  .remove or .pop
print(my_hobbies)

my_hobbies.pop(1)
print(my_hobbies)

my_hobbies.pop() # leaveing pop with nothing it removes the last elment
print(my_hobbies)

my_hobbies1 = ["code","food"]
add_hobbies = ["gym", "code again?"]
yes = my_hobbies + add_hobbies 
print(my_hobbies + add_hobbies)
print(yes)