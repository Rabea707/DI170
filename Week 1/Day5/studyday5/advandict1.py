#loops and dicts

my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
}

for x, y in my_books.items():
    print("the " + x + " is" + y)


#loops in range
print(list(range(1, 10, 2)))

#loops enumerate
for item in enumerate('abcd'):
    print(item)

for (index_count, letter) in enumerate('abcd'):
    print('At index {} the letter is {}'.format(index_count, letter))

for (index_count, letter) in enumerate("abcd"):
    print(f"at index {index_count} the letter is {letter}")
