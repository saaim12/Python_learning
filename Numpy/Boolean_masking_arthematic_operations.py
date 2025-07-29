import numpy as np
# The boolean mask is very useful when it comes to counting, modifying, extracting, or manipulating values in an array based on certain conditions or criteria. For example, the boolean mask can come in handy when we want to count all the values greater than a certain value. We can set a threshold and want to get rid of outliers in our data.
#
# In NumPy, boolean masking is often the most efficient way to accomplish these types of tasks. For example, boolean masking allows us to do the following:
#
# We can apply conditions such as >, <, ==, and so on.
# We can create a mask to filter out the even numbers in a NumPy array.

arr=np.arange(1,11)
masked_arr=arr >3
print(masked_arr)

#now getting arr from this mask

new_arr=arr[masked_arr]
print(new_arr)
# A number is even, if number % 2 is 0
mod_2_mask_1d = 0 == arr % 2
print("IsEven Array : ", mod_2_mask_1d )
#same we can do for 2d arrays


print(" ========= arthematic operations ========")
array1 = np.arange(0,5)
array2 = np.arange(0,5)

print("Actual Arrays (Array1): " , array1)
print("Actual Arrays (Array2): " , array2)

# Adding two arrays
print("Sum of arrays : ", (array1 + array2) )

# Subtracting two arrays
print("Subtraction of array : ", (array1 - array2) )

# Multiplication
print("Multiplication : ", (array1 * array2) )

# Division
print("Division : ", (array1 / array2) )
# warning and 0/0 is replaced with nan

# Power of all elements in the array
print("Power : ", (array1 ** 2) )

print("Actual Array : ", arr)
# Square root
print("Square Root : ", np.sqrt(arr))
# max and min values
print("Max : ", np.max(arr))
print("Min : ", np.min(arr))
# Trigonometric functions, e.g. sin, cos, tan, arcsin, ......
print("Sin : ", np.sin(arr))
# Calculate the exponential (e^) of all elements in the input array
print("Exponential : ", np.exp(arr) )
# log function
print("Log : ", np.log(arr) )
# warning for inf

# Convert angles from degrees to radians
print("Degree to Radians : ", np.deg2rad(arr) )

# Convert angles from radians to degrees
print("Radians to Degree : ", np.rad2deg(np.deg2rad(arr)) )