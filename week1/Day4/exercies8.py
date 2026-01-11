toppings = []

while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ")

    if topping == "quit":
        break

    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

base_price = 10
topping_price = 2.5
total_cost = base_price + len(toppings) * topping_price

print("\nYour pizza has the following toppings:")
for t in toppings:
    print("-", t)

print(f"Total cost: ${total_cost}")
