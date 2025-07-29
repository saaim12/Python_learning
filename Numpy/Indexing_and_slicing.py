import numpy as np
# 1-D arrays (vectors)
# In the simplest case, selecting one or more elements of the NumPy array works in a very similar way to Python lists. We can do the following in NumPy arrays:
#
# We can grab a value using the negative index (starts with -1). We can also do the same in Python lists.
#
# We can get a range from our NumPy array.
#
# We can also use the negative index to grab a range from our NumPy array.
#
# We can grab the values up to and from certain indexes of a NumPy array. We don’t need to give start and stop indices, since they’re optional.

my_arr=np.arange(1,20,2)
print(my_arr)

print("selecting one element " ,my_arr[4])
print("selecting element from behind ",my_arr[-3]) #-0 and 0 is same
print("selecting range ",my_arr[2:5])
print('The values from 1:-2 index range are: ', my_arr[1:-2])

print('Value in array_1d upto index 2 : ',my_arr[:2]) #all before 2 index
print('Value in array_1d from index 2 : ',my_arr[2:]) # all after 2 index
my_arr[0] = -102
# let's check what is at index 0 now!
print('Our Updated array is: ', my_arr)

# 2d arrays
print("----- 2d arrays ------")

my_arr2d=np.arange(20)
my_arr2d=my_arr2d.reshape(5,4)
print(my_arr2d)

# methods of selecting elements

print(my_arr2d[2,3])
print(my_arr2d[2][3])
#we can also apply slicing methods on this

print(my_arr2d[:2,2:])