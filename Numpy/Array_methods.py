import numpy as np
# creating two arrays
arange_arr=np.arange(1,10,dtype=int)
randint_arr=np.random.randint(1,12,10,dtype=int)

print('array using arange:',arange_arr)
print('array using randint: ',randint_arr)
#This method returns an array containing the same data as is passed to it but with a new shape.
print("----------- first method --------")
# compulsry: rows × columns = total elements in the array
print(arange_arr.reshape(3,3))
print("---------- second method --------")
array_randint = np.random.randint(0,100,10) # using randint()
print( array_randint )

print("Maximum : ",array_randint.max())
print("Minimum : ",array_randint.min())

print("Maximum element Index : ", array_randint.argmax() ) # index starts from 0

print("Minimum  element Index : ", array_randint.argmin() )

#Arrays in NumPy have a lot of attributes as well. Some of the most common and useful attributes are the following

print("size: ",array_randint.size)
print("shape : ",array_randint.shape)
print("dtype : ",array_randint.dtype)
