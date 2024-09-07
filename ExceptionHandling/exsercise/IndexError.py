list = [1,2,3,4,5,6]

index = int(input(f"Enter an index (0 to {len(list)-1}): "))

try:
    print(f"Element at position {index} is {list[index]}.")
except IndexError:
    print(f"Index {index} is out of bound")