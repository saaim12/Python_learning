#integer and float
x=5
y=6
z=6.55
print(x,y,z,x*z)
#strings they are imutable
name="saaim"
roll_no="FA21-BCE-096"
print("my name is {} and my roll no is {}".format(name,roll_no))
print(f'my name is {name} and my roll no is {roll_no}')
print(name[0])
print(roll_no[-1])
#methods of strings
String="hello world"
#slicing
# grabbing a slice (everything after index 1)
print(String[1:])
 # grabbing a slice (everything from index 0 upto 4 (not included))
print(String[:4])
print(String[3:4])
#spliting
print(String.split('e',3))
# lower cas and upper case
print(String.lower())
print(String.upper())
#concatination
new_name=name+" abdullah"
print(new_name)
# ascii chars
print(ord('A'))   # Output: 65
print(ord('a'))   # Output: 97
print(ord('0'))   # Output: 48
print(chr(65))    # Output: A
print(chr(97))    # Output: a
print(chr(48))    # Output: 0
