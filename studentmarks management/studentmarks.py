# Student Marks Management System

s = {}

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. Add Mark")
    print("3. View Student Average")
    print("4. View All Students")
    print("5. Class Average")
    print("6. Edit Student Name")
    print("7. Delete Student")
    print("8. Exit")

    c = input("Choose: ")

    # Add Student
    if c == "1":
        name = input("Student name: ")

        if name in s:
            print("Student already exists.")
        else:
            s[name] = {}
            print("Student added.")

    # Add Mark
    elif c == "2":
        name = input("Student name: ")

        if name in s:
            subject = input("Subject name: ")
            mark = float(input("Mark: "))

            if 0 <= mark <= 100:

                if subject in s[name]:
                    s[name][subject].append(mark)
                else:
                    s[name][subject] = [mark]

                print("Mark added.")

            else:
                print("Invalid mark.")

        else:
            print("Student not found.")

    # View Student Average
    elif c == "3":
        name = input("Student name: ")

        if name in s:

            total = 0
            count = 0

            for subject in s[name]:
                for mark in s[name][subject]:
                    total += mark
                    count += 1

            if count:
                print("Average =", round(total / count, 2))
            else:
                print("No marks.")

        else:
            print("Student not found.")

    # View All Students
    elif c == "4":

        if not s:
            print("No students.")

        else:
            for name in s:

                print("\nName:", name)

                for subject in s[name]:
                    print(subject, ":", s[name][subject])

    # Class Average
    elif c == "5":

        total = 0
        count = 0

        for name in s:
            for subject in s[name]:
                for mark in s[name][subject]:
                    total += mark
                    count += 1

        if count:
            print("Class Average =", round(total / count, 2))
        else:
            print("No marks.")

    # Edit Student Name
    elif c == "6":

        name = input("Current student name: ")

        if name in s:

            new_name = input("New student name: ")

            if new_name in s:
                print("Student already exists.")

            else:
                s[new_name] = s.pop(name)
                print("Student name updated.")

        else:
            print("Student not found.")

    # Delete Student
    elif c == "7":

        name = input("Student name to delete: ")

        if name in s:
            del s[name]
            print("Student deleted.")

        else:
            print("Student not found.")

    # Exit
    elif c == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")