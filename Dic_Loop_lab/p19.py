students = {}


def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


while True:
    print("\nStudent Record and Grade Manager")
    print("1. Add a student")
    print("2. Update a student's mark")
    print("3. Search by student ID")
    print("4. Display all students")
    print("5. Display student(s) with highest average")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter student ID: ")

        if student_id in students:
            print("Student ID already exists.")
        else:
            name = input("Enter student name: ")
            marks = []

            for i in range(3):
                while True:
                    mark = float(input("Enter mark " + str(i + 1) + ": "))

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break

                    print("Mark must be between 0 and 100.")

            students[student_id] = {
                "name": name,
                "marks": marks
            }

            print("Student added.")

    elif choice == "2":
        student_id = input("Enter student ID: ")

        if student_id not in students:
            print("Student not found.")
        else:
            print("Student:", students[student_id]["name"])

            for i in range(3):
                print(i + 1, ":", students[student_id]["marks"][i])

            mark_number = int(input("Enter mark number to update (1-3): "))

            if mark_number < 1 or mark_number > 3:
                print("Invalid mark number.")
            else:
                while True:
                    new_mark = float(input("Enter new mark: "))

                    if 0 <= new_mark <= 100:
                        students[student_id]["marks"][mark_number - 1] = new_mark
                        print("Mark updated.")
                        break

                    print("Mark must be between 0 and 100.")

    elif choice == "3":
        student_id = input("Enter student ID: ")

        if student_id in students:
            student = students[student_id]

            print("ID:", student_id)
            print("Name:", student["name"])
            print("Marks:", student["marks"])

            total = 0

            for mark in student["marks"]:
                total += mark

            average = total / 3

            print("Average:", average)
            print("Grade:", get_grade(average))
        else:
            print("Student not found.")

    elif choice == "4":
        if len(students) == 0:
            print("No students available.")
        else:
            for student_id, student in students.items():
                total = 0

                for mark in student["marks"]:
                    total += mark

                average = total / 3
                grade = get_grade(average)

                print(
                    student_id,
                    "-",
                    student["name"],
                    "Average:", average,
                    "Grade:", grade
                )

    elif choice == "5":
        if len(students) == 0:
            print("No students available.")
        else:
            highest_average = None
            highest_students = []

            for student_id, student in students.items():
                total = 0

                for mark in student["marks"]:
                    total += mark

                average = total / 3

                if highest_average is None or average > highest_average:
                    highest_average = average
                    highest_students = [student_id]
                elif average == highest_average:
                    highest_students.append(student_id)

            print("Highest average:", highest_average)

            for student_id in highest_students:
                print(
                    student_id,
                    "-",
                    students[student_id]["name"]
                )

    elif choice == "6":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")