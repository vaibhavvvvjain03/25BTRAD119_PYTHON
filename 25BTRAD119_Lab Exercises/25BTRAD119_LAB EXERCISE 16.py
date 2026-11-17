import random

while True:
    print("\n1.Roll One Die  2.Roll Two Dice  3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print("Dice result:", random.randint(1, 6))

    elif choice == "2":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print("Dice results:", die1, "and", die2)
        print("Total:", die1 + die2)

    elif choice == "3":
        break

    else:
        print("Invalid choice!")