fruits = ["apple","pear", "banana", "melon"]
print(len(fruits))

numbers = [3, 12, 1, -4]
print(sum(numbers))

numbers = [3, 5, 1, 2]
print(sorted(numbers))

#If you have strings, they will get sorted alphabetically.
letters = ['d', 'a', 'g', 'b']
print(sorted(letters))

#it will not work if you have mixed values.

#mixed = [3, 'd', 1, 'a']
#sorted(mixed)
#>> error!


food = ['spam', 'eggs', 'ham']
food.append('sushi')
print(food)


food.insert(0, 'beans')
print(food)

food.extend(['bread', 'water'])
print(food)
#######################
my_tuple = (5,6,7)
#tuples uses ()
#list uses []
a,b,c = my_tuple
print(a)