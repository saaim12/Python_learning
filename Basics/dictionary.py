# A dictionary is an object that stores a collection of data.
# Each element in a dictionary has two parts: a key and a value. We use keys to locate specific values.
a={1:"saaim",2:"sahal",3:"saboor"}
print(a)
#accessing specific value
print(a[1])
d2 = {'k1':[1,2,3],'k2':['a','b']}
print("list as Value : {}".format(d2['k1']))
print("list value of list in dict",d2['k2'][1])
#nested dict
nested_d = {'k1':{'k_in':[1,2,3]}}
# Printing dictionary
print("Dictionary : {}".format(nested_d))
# Printing the nested dictionary
print("Nested dictionary : {}".format(nested_d['k1']))
# Printing value from nested dictionary
print("Value from nested dictionary : {}".format(nested_d['k1']['k_in'][2]))
#methods of dict
# We have a dictionary
d1 = {'key1':'value1','key2':'value2', 'key3':'value3'}
# Grabbing all the keys.
print("Keys of dictionary : {}".format(d1.keys())) #try "list(d1.keys())"
# Grabbing all the values
print("Values of dictionary : {}".format(d1.values()))
# Grabbing all key-value pairs
print("Key-Value pairs of dictionary : {}".format(d1.items()))