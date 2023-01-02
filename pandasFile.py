import pandas as pd

df=pd.read_csv('pandastext.txt')
print(df)

print(df.info())
print(df.head(2))
print(df.tail(1))
print(df.to_numpy) #to convert pandas to numpy #it doesnt include index,coloumns in output
print(df.describe())
