
def trice(num):
    return num *3
# lambda: creates a small anonymous function
# Syntax: lambda arguments: expression
square = lambda x: x ** 2
print(square(5))  # Output: 25

# map: applies a function to each item in an iterable (like a list)
# Syntax: map(function, iterable)
nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)  # Output: [1, 4, 9, 16, 25]

# filter: filters items in an iterable based on a condition
# Syntax: filter(function_that_returns_bool, iterable)
even_nums = list(filter(lambda x: x % 2 == 0, nums))
#filter() expects the function to return True or False (i.e., a Boolean value) to decide whether to keep an element.


even_nums2 = list(filter(trice,[2,3,4,5,6,7,8,9]))

print(even_nums)  # Output: [2, 4]
print(even_nums2)
