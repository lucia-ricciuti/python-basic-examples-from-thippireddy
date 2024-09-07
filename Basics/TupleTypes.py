tpl = (20, 30, 20, 'xyz')
print(type(tpl))
print(tpl*3)
print(tpl.count(20))
print(tpl.index('xyz'))

# Convert list to tuple
lst=[10, 20, "Bharath", -10, 30.5]
print(type(lst))

tpl1 = tuple(lst)
print(tpl1)
print(type(tpl1))