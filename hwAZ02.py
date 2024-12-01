import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('school.csv')
print(df.head())
#print(df.tail())
print(df.info())
print(df.describe())

Q1_math = df['Math'].quantile(0.25)
Q3_math = df['Math'].quantile(0.75)
print('Q1_math = ',Q1_math,', Q3_math = ',Q3_math,', IQR = ',Q3_math-Q1_math)
#df.boxplot(column='math')
df['Math'].hist()
plt.show()
df.boxplot(column='Math')
plt.show()