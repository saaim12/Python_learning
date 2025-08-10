import pandas as pd


df = pd.read_csv("data.csv")  # This loads the CSV into a DataFrame
# print(df)
# print(df.info())
# print(df.isnull())
new=df[df.isnull()]
print(new)
print(new['Record Number'].value_counts(dropna=False))
