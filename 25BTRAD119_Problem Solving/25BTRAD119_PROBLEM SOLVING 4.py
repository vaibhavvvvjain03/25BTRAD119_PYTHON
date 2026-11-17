students = {}
classes = 0


def add_students():
    names = input("Enter student names separated by commas: ").split(",")

    for name in names:
        name = name.strip().title()

        if not name:
            continue

        if name in students:
            print(name, "already exists")
        else:
            students[name] = [None] * classes
            print(name, "added successfully")


def mark_attendance():
    global classes

    if not students:
        print("Add students first!")
        return

    classes += 1
    print("\nMark attendance: P = Present, A = Absent")

    for name in students:
        while True:
            status = input(name + " (P/A): ").strip().upper()

            if status in ("P", "A"):
                students[name].append(status)
                break
            else:
                print("Invalid input! Enter P or A.")

    print("Attendance recorded for Class", classes)


def update_attendance():
    name = input("Enter student name: ").strip().title()

    if name not in students:
        print("Student not found!")
        return

    records = students[name]
    valid_classes = [
        i for i, status in enumerate(records, start=1)
        if status in ("P", "A")
    ]

    if not valid_classes:
        print("No attendance records available.")
        return

    print("Attendance:", records)

    try:
        day = int(input("Enter class number to update: "))

        if day < 1 or day > len(records):
            print("Invalid class number!")
            return

        if records[day - 1] not in ("P", "A"):
            print("Attendance has not been marked for this class.")
            return

        status = input("Enter new status (P/A): ").strip().upper()

        if status not in ("P", "A"):
            print("Invalid status! Enter P or A.")
            return

        records[day - 1] = status
        print("Attendance updated successfully!")

    except ValueError:
        print("Enter a valid class number!")


def display_attendance():
    if not students:
        print("No students available.")
        return

    print("\n{:<20} {:<12} {:<12} {:<12}".format(
        "Student", "Present", "Absent", "Percentage"
    ))
    print("-" * 58)

    for name, records in students.items():
        valid = [r for r in records if r in ("P", "A")]
        present = valid.count("P")
        absent = valid.count("A")

        if valid:
            percentage = present / len(valid) * 100
            percent = str(round(percentage, 2)) + "%"
        else:
            percent = "N/A"

        print("{:<20} {:<12} {:<12} {:<12}".format(
            name, present, absent, percent
        ))


def attendance_percentage():
    name = input("Enter student name: ").strip().title()

    if name not in students:
        print("Student not found!")
        return

    valid = [r for r in students[name] if r in ("P", "A")]

    if not valid:
        print("No attendance records available.")
        return

    present = valid.count("P")
    percentage = present / len(valid) * 100

    print("\nStudent:", name)
    print("Present:", present)
    print("Absent:", valid.count("A"))
    print("Classes recorded:", len(valid))
    print("Attendance:", round(percentage, 2), "%")


def below_threshold():
    try:
        limit = float(input("Enter attendance threshold (%): "))

        if not 0 <= limit <= 100:
            print("Enter a percentage between 0 and 100.")
            return

        found = False
        print("\nStudents below", limit, "% attendance:")

        for name, records in students.items():
            valid = [r for r in records if r in ("P", "A")]

            if valid:
                percentage = valid.count("P") / len(valid) * 100

                if percentage < limit:
                    print(name, "-", round(percentage, 2), "%")
                    found = True

        if not found:
            print("No students below the threshold.")

    except ValueError:
        print("Enter a valid percentage!")


def class_summary():
    total_present = 0
    total_records = 0

    for records in students.values():
        valid = [r for r in records if r in ("P", "A")]
        total_present += valid.count("P")
        total_records += len(valid)

    print("\nTotal students:", len(students))
    print("Classes conducted:", classes)

    if total_records:
        percentage = total_present / total_records * 100
        print("Overall class attendance:", round(percentage, 2), "%")
    else:
        print("No attendance records available.")


def search_student():
    name = input("Enter student name: ").strip().title()

    if name in students:
        print("Student found:", name)
        print("Attendance records:", students[name])
    else:
        print("Student not found!")


while True:
    print("\n===== STUDENT ATTENDANCE TRACKER =====")
    print("1. Add Multiple Students")
    print("2. Mark Class Attendance")
    print("3. Update Attendance")
    print("4. Display All Attendance")
    print("5. Calculate Student Percentage")
    print("6. Find Students Below Threshold")
    print("7. Class Summary")
    print("8. Search Student")
    print("9. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        add_students()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        update_attendance()
    elif choice == "4":
        display_attendance()
    elif choice == "5":
        attendance_percentage()
    elif choice == "6":
        below_threshold()
    elif choice == "7":
        class_summary()
    elif choice == "8":
        search_student()
    elif choice == "9":
        print("Attendance Tracker closed.")
        break
    else:
        print("Invalid choice! Try again.")
