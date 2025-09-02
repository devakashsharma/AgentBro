score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

'''
The program checks the conditions from top to bottom. 
As soon as it finds a True condition, it executes that 
block of code and then skips the rest of the elif and else blocks.
'''