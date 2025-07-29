import numpy as np
array_1d = np.arange(0,10)
print("Original Array : ", array_1d)
array_1d[0:5] = 500
print("After Broadcasting : ", array_1d)

# same for 2d arrays
arrays_2d=np.ones((4,4))
print(arrays_2d)
print("\n After Broadcasting")
arrays_2d[0]=300
print(arrays_2d)
#simple 1-D array and broadcast it to array_2d
print( arrays_2d + np.arange(0,4) )

print("------------ fancy Indexing ----------")

my_arr_2d=np.arange(0,24).reshape(6,4)
print(my_arr_2d)
print("--------------------------------------")
#selecting multiple rows
print(my_arr_2d[[2,3,4]])