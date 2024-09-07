"""
list = []
for x in range(1,11):
    list.append(x**3)
print(list)
"""

list = [x**3 for x in range(1,11)]
print(list)
