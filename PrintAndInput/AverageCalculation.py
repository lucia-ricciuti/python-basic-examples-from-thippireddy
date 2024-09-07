from ntpath import sep
a,b,c=[int(n) for n in input("Enter three integer number separated by comma (','): ").split(sep=',')]

averageValue = (a+b+c) / 3;
print("The average value is:", averageValue)
