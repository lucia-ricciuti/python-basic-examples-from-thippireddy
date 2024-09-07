s={10,20,30,'xyz',10,20,10}
print(s)

s.update([88,99])
print(s)

s.remove(30)
print(s)

f=frozenset(s)
print(f)