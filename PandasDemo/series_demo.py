import pandas as pd

reviews = pd.Series([4.6, 4.4, 4.8, 5])

print("Reviews:",reviews)
print("First review:",reviews[0])
print("Describe")
print(reviews.describe())
print("Count:",reviews.count())
print("Mean:",reviews.mean())
print("Min:",reviews.min())
print("Max:",reviews.max())
print("Std:",reviews.std())

reviews = pd.Series([4.6, 4.4, 4.8, 5], index=['python','java','django','devops'])
print("Reviews:")
print(reviews)

reviews = pd.Series({'python':4.6, 'java':4.4, 'django':4.8, 'devops':5})
print("Reviews:")
print(reviews)

print("python:",reviews['python'])
print("python:",reviews.python)
print("java:",reviews.java)
print("django:",reviews.django)
print("devops:",reviews.devops)
print("values:",reviews.values)
print("index:",reviews.index)

courses = pd.Series(['Java','Python','AWS'])
print(courses)
print(courses.str.upper())
print(courses.str.contains('y'))