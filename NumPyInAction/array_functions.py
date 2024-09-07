from numpy import *
from numpy._core.fromnumeric import reshape

a1 = arange(12)
print("a1", a1)

a2 = reshape(a1, (2,6))
print("a2", a2)

a3 = reshape(a1, (2,2,3))
print("a3", a3)

print(a3.flatten())

print(eye(3))

print(zeros((2,3), int))
print(ones((2,3), int))