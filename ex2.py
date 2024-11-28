import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')
#print(df.head())
#print(df.tail())
#print(df.info())
#print(df.describe())
print(df.loc[56, 'Healthy life expectancy'])
print(df[df['Healthy life expectancy'] > 0.7])