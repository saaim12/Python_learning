import numpy as np
import pandas as pd

# creating data dictionary
data_dict = {'col_1':[1,2,3,4,5],
           'col_2':[111,222,333,111,555],
           'col_3':['alpha','bravo','charlie',np.nan,np.nan],
           }

# Creating DataFrame from data_dict
df = pd.DataFrame(data_dict,index=[1,2,3,4,5])
print(df) # let's have a look at what the DataFrame looks like!
print("No of unique values in df['col_1']:", df['col_1'].nunique())
print("No of unique values in df['col_2']:", df['col_2'].nunique())
print("No of unique values in df['col_3']:", df['col_3'].nunique())
print("\nvalue_count on df['col_1']:\n", df['col_1'].value_counts())
print("\nvalue_count on df['col_2']:\n", df['col_2'].value_counts()) #\n is just for new line in print()
print("\nvalue_count on df['col_3']:\n", df['col_3'].value_counts('charlie'))
# The sort_values() method is used to sort the values in a DataFrame. We can choose the column we want to sort the values by.
# By default, this method works with the following conditions in place:
# ascending = True
# inplace = False (True for permanent change)
print(df.sort_values(by = 'col_2'))
# Our customized function to calculate the squares
def square(value):
    return value**2

# This will return the square of "col_1"
print(df['col_1'].apply(square))
#OR
print(df['col_1'].apply(lambda value: value**2))
# Getting index of the DataFrame
print("Index \n", df.index)
# Getting column names
print("Columns \n", df.columns)
# Deleting row (axis=0) or column (axis=1)
df.drop('col_1',axis=1)
# we did not pass inplace = True in the above code using drop(), so the change will not be the permanent
print("\nAfter Deletion", df) # inplace = True for permanent change

# deleting col_1 permanently
newdf= df.copy() # creating a copy, may need to use df at later stage
del newdf['col_1']
print("\nPermanent delete\n", newdf)
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

foobar = pd.DataFrame(data)
print(foobar.pivot_table(values='D',index=['A', 'B'],columns=['C']))