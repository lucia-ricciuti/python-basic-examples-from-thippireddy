dict1 = {1:"John", 2:"Bob", 3:"Mark"}
print(dict1)
print(dict1.items())

keys = dict1.keys()
for i in keys: print(i)

values = dict1.values()
for i in values: print(i)

print(dict1[3])

del dict1[2]
print(dict1)