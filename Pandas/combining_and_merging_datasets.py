import numpy as np
import pandas as pd
df1 = pd.DataFrame({'key': ['a', 'b', 'c', 'd', 'e'],'A1': range(5), 'B1':range(5,10)})
df2 = pd.DataFrame({'key': ['a', 'b', 'c'], 'A2': range(3), 'B2':range(3,6)})
print("Dataframe 1\n", df1)
print("Dataframe 2\n", df2)
df1.index.name="index"
df2.index.name="index"
print("Dataframe 1\n", df1)
print("Dataframe 2\n", df2)
# There are several parameters that we can pass to the merge() method. The most important ones are how and on, which we’ll discuss here.
#
# The how method tells merge() what type of joining operation needs to be done.
# The joining operation could be inner, outer, left, or right. The default value of how is inner.
# The on method specifies what field name to join on. This could be a label or a list.


# Keeps only rows where 'key' exists in BOTH df1 and df2.
# Keys present in both: 'a', 'b', 'c'
print("\nmerged (how = 'inner'): \n",pd.merge(df1, df2, how = 'inner', on='key'))
# Keeps all rows from both DataFrames.
# Fills missing values with NaN where a match is not found.
print("\nmerged (how = 'outer'): \n",pd.merge(df1, df2, how = 'outer', on='key'))
print("\nmerged (how = 'left'): \n",pd.merge(df1, df2, how = 'left', on='key'))
print("\nmerged (how = 'right'): \n",pd.merge(df1, df2, how = 'right', on='key'))
# creating two DataFrames, left and right
left = pd.DataFrame({'key1': ['a', 'a', 'b', 'c'],
                     'key2': ['a', 'b', 'a', 'b'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['a', 'b', 'b', 'c'],
                      'key2': ['a', 'b', 'a', 'a'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print("left is :\n", left)
print("\nright is :\n", right)
print("\nmerged (inner) on key1 and key2 is :\n", pd.merge(left, right, how='inner', on=['key1', 'key2']))
print("\nmerged (outer) on key1 and key2 is :\n", pd.merge(left, right, how='outer', on=['key1', 'key2']))
print("\nmerged (left) on key1 and key2 is :\n", pd.merge(left, right, how='left', on=['key1', 'key2']))
print("\nmerged (right) on key1 and key2 is :\n", pd.merge(left, right, how='right', on=['key1', 'key2']))
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
''' 
  notice the NaN in the final DataFrame! K1 is not in "right", 
  missing data for this key!
'''
print(left.join(right))
'''
  notice the NaN in the final DataFrame! Now, K3 is not in "left", 
  missing data for this key!
'''
print(right.join(left))