import pandas as pd
df=pd.read_csv("C:/Users/user702/PycharmProjects/pythonProject/pokemon_data.csv")
print(df)
#print(df.tail(5))
df_text=pd.read_csv("pokemon_data.txt",delimiter='\t')
print(df_txt.head(5))
print(df.iloc[0.4])
for index,row in df.iterrows():
    print(index(index,row['Name'])
df.loc[df['Type1']]

