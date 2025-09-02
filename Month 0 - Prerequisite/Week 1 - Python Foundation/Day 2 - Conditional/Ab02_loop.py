# For Loop:
# Looping through a list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Looping through a range of numbers:
for number in range(1, 5):  # This will generate numbers from 1 up to (but not including) 5
    print(number)

# While Loop
count = 0
while count < 3:
    print("The count is:", count)
    count = count + 1  # This line is crucial to eventually make the condition False

# We can use special keywords to control the flow within loops:
# break: This statement immediately exits the current loop, regardless of the loop's condition.
for number in range(1, 10):
    if number == 5:
        break  # Stop the loop when number is 5
    print(number)

# continue: This statement skips the rest of the code in the current iteration and moves on to the next one.
for number in range(1, 6):
    if number == 3:
        continue  # Skip printing 3
    print(number)