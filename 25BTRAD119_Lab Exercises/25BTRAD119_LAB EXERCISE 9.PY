students = {}
names = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    names.append(name)
    students[name] = marks

for name in names:
    marks = students[name]

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    print(name, marks, grade)