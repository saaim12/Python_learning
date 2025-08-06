#list like array in other languages
my_list=[1,2,3,4]
print(len(my_list))
list_of_string = ['d','e','f']
print(f"list of chars ={list_of_string}")
# grab the first item in the list
print("First element in the List : {}".format( my_list[0] ))
# grab everything after first element
print("Everything after first element : {}".format( my_list[1:] ))
# grab a slice from index location 1 to 2, but not including the element at index 3
print("A slice from index location 1 to 2: {}".format( my_list[1:3] ))
#nesting in list
nested_list=[1,2,[2,3,['1','2']]]
print(nested_list)
print(nested_list[2][2])
print(nested_list[2][2][1])