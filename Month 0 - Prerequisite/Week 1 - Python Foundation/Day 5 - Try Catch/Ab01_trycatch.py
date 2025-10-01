# The try...except block is used to handle exceptions in Python. Here's the syntax of try...except block:
# syntax
# try:
    # code that may cause exception
# except:
    # code to run when exception occurs

try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0. 

# For each try block, there can be zero or more except blocks. Multiple except blocks allow us to handle each exception differently.
try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")

# Output: Index Out of Bound

# Python try with else clause
# In some situations, we might want to run a certain block of code if the code block inside try runs without any errors.

# For these cases, you can use the optional else keyword with the try statement.

# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

# Python try...finally
# In Python, the finally block is always executed no matter whether there is an exception or not.

# The finally block is optional. And, for each try block, there can be only one finally block.

try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)
except:
    print("Error: Denominator cannot be 0.")
finally:
    print("This is finally block.")