#while loop
i=0
while i<5:
    print(i)
    i=i+1

#for loop
my_list = [1,2,3,4,5]
for num in my_list:
  print('Hello world')

# range function
# The code below gives the range object, which is iterable.
print(range(5))

# We convert the range object into a list with the list method
print(list(range(5)))

# Use of range(), with single argument, in a loop
print("Use of range(), with single argument, in a loop")
for i in range(5):
  print(i)

# Use of range(), with two argument, in a loop
print("Use of range(), with two argument, in a loop")
for i in range(3,5):
  print(i)

# Use of range(), with three argument, in a loop
print("Use of range(), with three argument, in a loop")
for i in range(1,10,2):
  print(i)
#list comprehension
# We have a list x
x = [2,3,4,5]
# So, this is going to be our first list comprehension to compute squares of all
# the elements in a given list!
out = [num**2 for num in x]
print(out)
squares = [numbers**2 for numbers in range(2,10)]
print(squares)