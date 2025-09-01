# Tuples is the same as the list but the only thing in is this, tuple are immutable, means we cannot change it's value

# ways to create
names = ('naruto', 'naruto shippuden', 'erased', 'death note')

# names[0] = 'Itachi' # This will cause an error because tuples are immutable, we can't change it

# use a constructor
names2 = tuple(('one piece', 're-zero', 'spyxfamily'))

name3 = ('Light')
name4 = ('Naruto',)
print(name3, name4) # the only difference is that, if we have only one value in our tuple then it consider it as a string but if we use ',' after the value then it is consider them as a tuple

print(names2[2])

# del name3 # it will delete the name3 variable
# print(names3)
print(len(names))