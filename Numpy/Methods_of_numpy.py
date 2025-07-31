import numpy as np

# 1: The arange() method is very similar to the Python function range().
# It returns evenly spaced values within a given interval. The syntax of the arange() method is as follows:
#arange([start,] stop[, step,], dtype=None)
# similar to range() in Python, up to but not including 10
print( np.arange(0,10) )

# We can give a step (2 in this case)
print( np.arange(0,11,2) )

# We can give the step and dtype
print( np.arange(0,10,2, dtype=float) )

my_list=np.arange(12,100,2)
print(my_list)

print("------------------- 2nd Method ---------------")

# 2: The linspace() method returns evenly spaced numbers over a specified interval.
# start from 1 & end at 15 with 10 evenly spaced points b/w 1 to 15.
print( np.linspace(1, 15, 150,dtype=int) )

# Let's find the step size with "retstep" which returns the array and the step size
#retstep=True tells NumPy to also return the spacing (step size) between values.
my_linspace = np.linspace(5, 15, 9, retstep=True)
#------------------------(start ,stop , no of numbers in that interval)-----
print( my_linspace )

# We can grab array and step size separately.
print('array is: ',my_linspace[0],type(my_linspace[0]))
print('stepsize is: ', my_linspace[1],type(my_linspace))
#In the case of the arange() method, the second argument is not included in the array,
# but in the case of linspace(), the second argument is included.

print("----------------- 3rd Method ----------------")
print("We can use the zeros() method to create an array with all zeros.")
# 1-D array with 3 elements (zeros)
print( np.zeros(3) )

# Creating 2-D array, (no_row, no_col) passing a tuple
print( np.zeros((4,6)) )

print(" Same for ones")
# 1-D array with 3 elements (ones)
print( np.ones(3) )

#Creating 2-D array, (no_row, no_col) passing a tuple
print( np.ones((4,6)) )

print("to create identity matrix we use eye")
print(np.eye(5,dtype=int))

print("---------- 4 th method --------")
# 1-D array with three elements
print ( np.random.rand(3) )

# row, col, note we are not passing a tuple here
# each dimension (num_of_rows, num_of_columns) is a separate argument
print(np.random.rand(3,2))

#returns one random int, 1 inclusive, 100 exclusive
print( np.random.randint(1,100) )

#returns ten random int,
print( np.random.randint(1,100,10) )