# 1. Initialize the student marks tracker
student_marks = {}

# 2. Add/Update marks using a while loop
print(f"Enter marks to add\nType 'done' when finish")

while True:
    subject = input(f"Enter Subject Name: ").strip().title()
    if (subject == "Done"):
        break

    # Use a try-except block to handle non-integer input
    try:
        mark = int(input(f"Enter mark for {subject}: "))
        # Ensure the mark is within a reasonable range
        if 0 <= mark <= 100:
            student_marks[subject] = mark
            print(f"Marks has been recorded for {subject}")
        else:
            print("Enter marks between 0 and 100")
    except ValueError:
        print("Invalid input. Please enter a number for the mark.")

if not student_marks:
    print(f"No marks were entered. Exiting program.")
else:
    # 3. Calculate the average
    # Dictionaries store keys and values. We only need the values (the marks) for the calculation.
    total_marks = sum(student_marks.values())
    total_subjects = len(student_marks)
    avg_marks = total_marks / total_subjects

    # 4. Display the results
    print(f"subject : mark")
    for subject, mark in student_marks.items():
        print(f"{subject} : {mark}")
    
    print("-----------------------------")
    print(f"Average Marks: {avg_marks:.2f}")