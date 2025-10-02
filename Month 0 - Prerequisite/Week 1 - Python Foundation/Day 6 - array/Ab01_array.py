# What is an Array in Python?
# An array is basically a data structure which can hold more than one value at a time. It is a collection or ordered series of elements of the same type.
	
a=arr.array('d',[1.2,1.3,2.3])

# Is Python list same as an Array?
# Python Arrays and lists are store values in a similar way. But there is a key difference 
# between the two i.e the values that they store. A list can store any type of values such 
# as intergers, strings, etc. An arrays, on the other hand, stores single data type values.
# Therefore, you can have an array of integers, an array of strings, etc.

# Python also provide Numpy Arrays which are a grid of values used in Data Science. You can look into Numpy Arrays vs Lists to know more.

# Syntax:

a=arr.array(data type,value list) #when you import using arr alias
a=array(data type,value list)               #when you import using *

# Adding/ Changing elements of an Array:
a=arr.array('d', [1.1 , 2.1 ,3.1] )
a.append(3.4)
print(a)

a=arr.array('d', [1.1 , 2.1 ,3.1] )
a.extend([4.5,6.3,6.8])
print(a)

a=arr.array('d', [1.1 , 2.1 ,3.1] )
a.insert(2,3.8)
print(a)

# Array Concatenation :
a=arr.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])
b=arr.array('d',[3.7,8.6])
c=arr.array('d')
c=a+b
print("Array c = ",c)

# Removing/ Deleting elements of an array:
a=arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
print(a.pop())
print(a.pop(3))

a=arr.array('d',[1.1 , 2.1 ,3.1])
a.remove(1.1)
print(a)

# Slicing an array :
a=arr.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])
print(a[0:3])

# Looping through an array:
a=arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
print("All values")
for x in a: 
print(x)
print("specific values")
for x in a[1:3]: 
print(x)

# Reference: https://www.edureka.co/blog/arrays-in-python