name = input("Enter student name: ")

m1 = int(input("Enter marks in Python: "))
m2 = int(input("Enter marks in Maths: "))
m3 = int(input("Enter marks in English: "))

total = m1 + m2 + m3
percentage = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: F")