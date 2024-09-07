availableToppings = {
    1: "Onions",
    2: "Lettuce",
    3: "Tomatoes",
    4: "Olives",
    5: "Peppers"
}


repeatedIterations = range(3);
choosenToppings = []

print("Available toppings: ", availableToppings)
print("Pick three toppings.")
for i in repeatedIterations:
    choosenToppings.append(int(input("Enter the number that identifies the topping (1/2/3/4/5): ")))
quantity = int(input("How many sandwiches? "));

totalPrice = quantity * 5;

print("--- Receipt")
print(f"{quantity} sandwiches at 5$ each = {totalPrice}$")
print("Toppings: ")
for toppingId in choosenToppings:
    print(availableToppings[toppingId])