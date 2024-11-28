import pandas as pd
df = pd.read_csv('animal.csv')
print(df)
#df.fillna(value = 0, inplace=True)
#print(df)
#df.dropna(inplace=True)
group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)
