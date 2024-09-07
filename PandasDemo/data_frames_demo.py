import pandas as pd

scores_dict = {'Kohli':[100,50,70], 'Rohit':[100,88,0], 'Surya':[77,110,0], 'Jadeia':[99,120,8]}

#scores = pd.DataFrame(scores_dict, index=['I1','I2','I3'])
scores = pd.DataFrame(scores_dict, index=['I1','I2','I3'])
scores.index = ['I1','I2','I3']
print("Scores")
print(scores)

print("Kohli Scores")
print(scores['Kohli'])
print(scores.Kohli)

print("Scores by row")
print(scores.loc['I1'])
print(scores.iloc[1])
print(scores.loc['I1':'I3'])
print(scores.iloc[0:2])

print(scores.loc[['I1','I3']])
print(scores.iloc[[0,1]])

print("Scores by row and column")
print(scores.loc['I1':'I2', ['Kohli', 'Surya']])
print(scores.iloc[[0,2], 0:3])

print(scores[scores >= 90])
print(scores[(scores >= 80) & (scores <= 0)])

print("Scores at I2,Kohli:",scores.at['I2', 'Kohli'])
print("Scores at 2,0:",scores.iat[2,0])

scores.at['I2','Kohli'] = 150
print("Scores at I2,Kohli:",scores.at['I2', 'Kohli'])

scores.iat[2,0] = 200
print("Scores at 2,0:",scores.iat[2,0])

print(scores)
print("Mean")
print(scores.mean())
print("Describe")
pd.set_option('display.precision',2)
print(scores.describe())
print(scores.T)
print(scores.T.describe())

print(scores.sort_index(ascending=False))
print(scores.sort_index(axis=1, ascending=False))
print(scores.sort_values(by='I1', axis=1, ascending=False))

