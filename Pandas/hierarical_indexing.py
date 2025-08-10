# Importing numpy and Pandas first
import numpy as np
import pandas as pd

# Set a random seed for reproducibility
np.random.seed(42)  # You can use any integer as the seed value

# Create a Series with a list of lists (or arrays) as the index:
index = [['a','a','a','b','b','b','c','c','d','d'], # level 1 index
         [1,2,3,1,2,3,1,2,1,2]] # level 2 index

# Let's create a Series "ser" with multi-level index (2 in this example)
ser = pd.Series(np.random.randn(10), index=index)
print(ser)
print("first df",ser.loc['a'][1])
df2=pd.DataFrame(np.arange(12).reshape(4,3),index=[['a','a','b','b'],[1,2,1,2]],columns=['AB','ON','BC'])
print("============> df2 \n",df2)
print(df2.loc[['a','b'],['AB']])
#selective values
print(df2.loc['b'].iloc[0]['ON'])
print("+++++++++++++++")
print(df2.index.names) # no names
#giving names
df2.index.names=['L1','L2']
print(df2)

print("The xs() method  Let’s introduce a very useful and built-in method. \n "
      "The xs() method helps us grab data from a multilevel index—even from inside it.\n"
      " Grabbing all the data in df, whose index L_2 is 1, may be tricky for the loc method.\n "
      " In this case, xs is the more suitable method to do the job. For example, we can tell xs() what we want to grab (1 here means column) and indicate the level (L_2) to grab it from.")
print(df2.xs('a'))
print("???????")
print(df2.xs(1, level='L2')) # means l_2 column and 1 row of each