names = []
contacts = {}

while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        names.append(name)
        contacts[name] = phone

    elif ch == 2:
        name = input("Enter name: ")
        print(contacts.get(name, "Not found"))

    elif ch == 3:
        name = input("Enter name: ")
        if name in contacts:
            contacts[name] = input("Enter new phone: ")
        else:
            print("Not found")

    elif ch == 4:
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
            names.remove(name)
            print("Deleted")
        else:
            print("Not found")

    elif ch == 5:
        for name in names:
            print(name, contacts[name])

    elif ch == 6:
        break