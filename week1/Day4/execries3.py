basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.pop()
print(basket)
basket.pop(2)
print(basket)
basket.append("kiwi")
print(basket)
basket.insert(0,"Apples")
print(basket)
count =+ 0
for a in basket:
    if a == "Apples":
        count += 1

print(count)
print(basket.count("Apples"))
# both works im not used to python a lot hahah 
basket.clear()
print(basket)
