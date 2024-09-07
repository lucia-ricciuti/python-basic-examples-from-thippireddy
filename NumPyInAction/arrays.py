from numpy import *
from numpy._core._multiarray_umath import dtype
from numpy._core.function_base import linspace

arr = array([1,2,3,4,5], int)
carr = array(['a','b','c','d'])
sarr = array(['Python','Django','Django Rest'], dtype=str)
print(arr)
print(carr)
print(sarr)

print("linspace=",linspace(0,100,5))
print("logspace=", logspace(1,20));
print("arange=", arange(1,20))
print("arange=", arange(20,1,-2))
print("zeros=", zeros(10))
print("ones=", ones(10))