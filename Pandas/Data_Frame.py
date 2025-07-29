# create data frame from scratch
import numpy as np
import pandas as pd

columns="c1 c2 c3 c4 c5 c6 c7 c8 c9 c10".split()
rows="r1 r2 r3 r4 r5 r6 r7 r8 r9 r10".split()
data=np.arange(0,100).reshape(10,10)

df=pd.DataFrame(data=data,index=rows,columns=columns)
print(df)
#grabing columns it dont work with rows to access rows we use loc func
print(df["c1"])
print(df[["c1","c10"]])
print(df.c1,df.c2)
df["new"]=df.c1+df.c5
print(df)

#deleting column
df.drop(['c1'], axis = 1, inplace = True)
# If we don't pass inplace = True, then change will not be permanent
print(df)
print("___________ accessing rows __________")
# We can retrieve a row by its name or position with loc and iloc.
#
# To access a row by label(s), we use loc.
# To access a row using the row’s index location, we use iloc.

print(df.loc[['r2', 'r3']])
print(df.iloc[[1, 2]]) # remember, index starts with 0

print("Grabbing a subset of a DataFrame means a specific element ")
print("Element at r1,c1 : ", df.loc['r1','c2'])
print("Element at r2,c2 : ", df.loc['r2', 'c10'])

# for a subset, pass the list
print("Subset \n",df.loc[['r1','r2'],['c10','c2']])

# another example - random columns and rows in the list
print("Random Columns and Rows \n", df.loc[['r2','r5'],['c3','c4']])
# We can do a conditional selection as well
print(df > 5)
print(df!=99)

#boolean masking like we did in numpy
bool_mask=df % 2==0
print(bool_mask)
df2=df[bool_mask]
print(df2)
print(df[['c7']] > 11)
# We need two rows, pass in a list of those rows
print("Rows \n",df[df['c6']>11].loc[['r3','r5']])

print("______________ useful methods ___________")
print("\n Combined Conditions \n",df[(df['c7']>60) & (df['c2']>80)])
# inplace = True for permanent change
print("Reset index \n",df.reset_index(inplace = True))
# split at white spaces, newind is our list of alphabets
newind = 'a b c d e f g h i j'.split()
# let put newind as a new col in the df
df['newind']=newind
print("New column added \n ",df)
#setting newind as an index, needs to be inplaced
df.set_index('newind', inplace = True)
print("Inplaced newint \n", df)

print("First 2 Rows \n ", df.head(n=2)) # n=5 by default
print("Last 2 Rows \n", df.tail(n=2)) # n=2 by default

print("Dataframe info \n", df.info())

print("Described Dataframe \n", df.describe())

print(df.drop(["index"],axis=1,inplace=True))
print(df.mean())