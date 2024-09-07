from _functools import reduce
prices = {
    "banana": 0.50,
    "apple": 0.30,
    "milk": 1.20,
    "bread": 2.00
}

repeatRange = range(3)
itemNames = []
itemQuantities = []
itemPrices = []

for i in repeatRange:
    itemNames.append(input("Enter the name of the item (Banana/Apple/Milk/Bread): ").lower());
    itemQuantities.append(int(input("Quantity (default 1): ") or "1"));
    itemPrices.append(prices[itemNames[i]]*itemQuantities[i]);

subTotal = reduce(lambda a, b: a+b, itemPrices)
taxes = subTotal * 0.085;
totalPrice = subTotal + taxes;

print("--- Receipt")
for i in repeatRange:
    print(f"{itemNames[i].capitalize()}: {itemQuantities[i]} @${prices[itemNames[i]]:.2f} each = ${itemPrices[i]:.2f}")
print(f"Subtotal: ${subTotal:.2f}");
print(f"Taxes: ${taxes:.2f}");
print(f"Total Price: ${totalPrice:.2f}");
