lst=[20,30,40,234]
print(type(lst))

b=bytes(lst)
print(type(b))

ba=bytearray(lst)
print(type(ba))
ba[2] = 33