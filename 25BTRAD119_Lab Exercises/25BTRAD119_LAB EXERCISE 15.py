class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print("Book issued:", self.title)
        else:
            print("Book is not available!")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned:", self.title)
        else:
            print("Book was not issued!")

    def display(self):
        status = "Available" if self.available else "Issued"
        print(self.title, "-", status)


books = [Book("Python"), Book("Java"), Book("C Programming")]

while True:
    print("\n1.Display  2.Issue  3.Return  4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        for book in books:
            book.display()

    elif choice in ("2", "3"):
        title = input("Enter book title: ").strip().lower()

        for book in books:
            if book.title.lower() == title:
                if choice == "2":
                    book.issue()
                else:
                    book.return_book()
                break
        else:
            print("Book not found!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")