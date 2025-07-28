import numpy as np
# for checking version
print(np.__version__)

# we can create numpy arrays from python lists

my_list=[1,2,3,4]
print(my_list,type(my_list))

my_np_arr=np.array(my_list)
print(my_np_arr,type(my_np_arr))

# same for 2d arrays
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print( my_matrix )
# Two-dimensional array from Matrix
matrix_one = np.array(my_matrix)
print(matrix_one,type(matrix_one))

# We can use Tuple instead of a list as well.
my_tuple = (-1,0,1)
my_array = np.array(my_tuple)
print( my_array, type(my_array) )