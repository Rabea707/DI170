tuples = (33,22,11)
#Given a tuple of integers, try to add more integers to the tuple.
#Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
#well you cant change it since its immutable *tuples.append(44) 
# but there is a way 
new_item = (44, )
new_tuples = tuples + new_item
print(new_tuples)