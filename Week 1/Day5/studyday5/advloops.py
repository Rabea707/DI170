#zip(iterable,..) : concat [iterables, …] in a tuple.
list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

for item in zip(list1, list2, list3): # only go as far it is possible
    print(item)

#else
for i in range(1, 3):
    print(i)
else:print("the loop is over")


#while some_condition:
    # do something
#else:
    # do another thing
x = 0
while x < 2:
    print(f'x is {x}')
    x += 1
else:
    print('x is bigger than 2')

#Break, Continue, Pass
for letter in 'Leonardo':
    if letter == 'a':
        break
    print(letter, end='') # end='' renders each letter next to the other
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')

#continue: return to the top of the loop (continue to the next iteration of the loop)
for letter in 'Leonardo':
    if letter == 'o':
        continue
    print(letter, end='') # dont execute for 'o' letter
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
for item in [1,2,3]:
    # comment
    pass # to avoid the error

print('Finish the script')

