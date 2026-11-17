import os

filename = "students.txt"


def add_student():
    roll = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()
    marks = input("Enter marks: ").strip()

    if not roll or not name:
        print("Roll number and name cannot be empty.")
        return

    try:
        marks = float(marks)
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Enter valid marks.")
        return

    records = read_students()

    if any(s[0] == roll for s in records):
        print("Roll number already exists.")
        return

    with open(filename, "a") as file:
        file.write(f"{roll},{name},{marks}\n")

    print("Student added successfully!")


def read_students():
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        return [line.strip().split(",") for line in file if line.strip()]


def display_students():
    records = read_students()

    if not records:
        print("No student records found.")
        return

    print("\nRoll No\tName\tMarks")
    for s in records:
        print(s[0], "\t", s[1], "\t", s[2])


def search_student():
    roll = input("Enter roll number to search: ").strip()

    for s in read_students():
        if s[0] == roll:
            print("Roll No:", s[0])
            print("Name:", s[1])
            print("Marks:", s[2])
            return

    print("Student not found.")


def update_student():
    roll = input("Enter roll number to update: ").strip()
    records = read_students()

    for s in records:
        if s[0] == roll:
            name = input("Enter new name: ").strip()
            marks = input("Enter new marks: ").strip()

            if not name:
                print("Name cannot be empty.")
                return

            try:
                marks = float(marks)
                if not 0 <= marks <= 100:
                    print("Marks must be between 0 and 100.")
                    return
            except ValueError:
                print("Enter valid marks.")
                return

            s[1] = name
            s[2] = str(marks)

            with open(filename, "w") as file:
                for record in records:
                    file.write(",".join(record) + "\n")

            print("Student updated successfully!")
            return

    print("Student not found.")


while True:
    print("\n===== STUDENT DATA MANAGER =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        print("Program closed.")
        break
    else:
        print("Invalid choice.")