name=input("Enter your name: ")
print(f"Your name is {name}.")

age = int(input("Enter your age: "))
print(f"Your age is {age}")
print(type(age))

lst = [float(x) for x in input("Enter three decimal numbers separated by comma: ").split(",")]
print(lst)