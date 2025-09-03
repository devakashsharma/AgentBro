# dictionary is an unordered collection of items that stores data in key-value pairs
# A simple dictionary
student = {
    "name": "Alice",
    "age": 25,
    "courses": ["History", "Math"]
}

# An empty dictionary
empty_dict = {}

# access to the element
# using []
print(student["name"])  # Output: Alice

# Attempting to access a non-existent key will raise a KeyError
# print(student["address"])  # This would cause an error

# using .get()
# Get a value that exists
print(student.get("age"))  # Output: 25

# Get a value that doesn't exist (returns None)
print(student.get("address"))  # Output: None

# Get a value that doesn't exist, with a default value
print(student.get("address", "Not Found"))  # Output: Not Found

# Modifying Dict
# Adding a new key-value pair
student["gpa"] = 3.8
print(student)
# Output: {'name': 'Alice', 'age': 25, 'courses': ['History', 'Math'], 'gpa': 3.8}

# Updating an existing value
student["age"] = 26
print(student)
# Output: {'name': 'Alice', 'age': 26, 'courses': ['History', 'Math'], 'gpa': 3.8}

# Removing
# using 'del'
del student["gpa"]
print(student)
# Output: {'name': 'Alice', 'age': 26, 'courses': ['History', 'Math']}

# using .pop()
# pop() also returns the value of the removed item
age_removed = student.pop("age")
print(age_removed)  # Output: 26
print(student)
# Output: {'name': 'Alice', 'courses': ['History', 'Math']}

# Methods
print(student.keys())
# Output: dict_keys(['name', 'age', 'major'])

print(student.values())
# Output: dict_values(['Alice', 25, 'Computer Science'])

print(student.items())
# Output: dict_items([('name', 'Alice'), ('age', 25), ('major', 'Computer Science')])
