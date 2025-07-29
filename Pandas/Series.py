#there are two data structures in python
# A Series is a one-dimensional,
# array-like object containing values and an array of labels associated with the values. Series can be indexed using labels.
import numpy as np
import pandas as pd

my_labels=["x","y","z"]
my_data = [100,200,300]

# Converting my_data (Python list) to pandas Series
print(pd.Series(data = my_data))
# for editing labels values

print(pd.Series(data=my_data,index=my_labels))

#same we can do with numpy arrays

arr=np.arange(1,3)
print(pd.Series(arr,["a","b"]))
my_dict = {'x':100,'y':200,'z':300}
# If we pass a dictionary to Series, pandas will take the keys as index/labels and values as data.
print(pd.Series(my_dict))
print(pd.Series(my_labels))
# We can pass a list of built-in functions!
print(pd.Series([min, max, sum, print]))


dict_1 = {'Toronto': 500, 'Calgary': 200, 'Vancouver': 300, 'Montreal': 700}
dict_2 = {'Calgary': 200, 'Vancouver': 300, 'Montreal': 700}
dict_3 = {'Calgary': 200, 'Vancouver': 300, 'Montreal': 700, 'Jasper':1000}

# Creating Pandas Series from the dictionaries
ser1 = pd.Series(dict_1)
ser2 = pd.Series(dict_2)
ser3 = pd.Series(dict_3)

print(ser1,ser2,ser3)
#grabbing one item from series
print(ser1['Calgary'])
#imp point
# When we’re only passing a dictionary, the index in the resulting Series will have the dictionary’s keys in sorted order (in this case, C, M, T, and V are sorted in this order).
# We can override this by passing the dictionary keys in the order we want them to appear in the resulting Series.
# if one will have not same key it will not be added only key is remained
ser3=ser1+ser2
print(ser3)
# Basic operations on Series are usually based on the index. For example, if we want to add ser1 and ser2, pandas tries to match up the operation based on the index. For Calgary, Montreal, and Vancouver,
# it adds the values—but for Toronto it can not find a match and therefore puts NaN there.

print("_______________ methods _____________")
#The isnull() method in Series is used to detect missing data.
print(ser3.isnull())
print("Head : \n",ser1.head(2)) # head(1) will return the first row only
print("Tail : \n",ser1.tail(1)) # tail(1) will return the last row only
print("\n it will return the indexes values")
print("Axis : ", ser1.axes)

print("\n it will return the values")
print("Values : ", ser1.values)

print("Size : ", ser1.size)

# True for empty Series
print("Is Empty ? ",ser1.empty)