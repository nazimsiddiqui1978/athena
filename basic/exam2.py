# Initialize dictionary
student_grades = {}

while True:
    print("\nOptions:")
    print("1. Add new student and grade")
    print("2. Update existing student grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in student_grades:
            print(f"{name} already exists with grade {student_grades[name]}")
        else:
            grade = input("Enter grade: ")
            student_grades[name] = grade
            print(f"Added {name} with grade {grade}")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print(f"Updated {name}'s grade to {grade}")
        else:
            print(f"{name} not found in the record.")

    elif choice == "3":
        if not student_grades:
            print("No student records found.")
        else:
            print("\nStudent Grades:")
            for student, grade in student_grades.items():
                print(f"{student}: {grade}")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")