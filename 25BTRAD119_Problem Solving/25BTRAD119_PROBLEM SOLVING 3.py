
sales = {}

while True:
    print("\n===== SALES DATA ANALYZER =====")
    print("1. Add Sales")
    print("2. Display Sales")
    print("3. Calculate Total Sales")
    print("4. Find Best-Selling Product")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        product = input("Enter product name: ").strip().title()

        try:
            quantity = int(input("Enter quantity sold: "))
            price = float(input("Enter price per unit: "))

            if not product or quantity <= 0 or price < 0:
                print("Enter valid product details.")
            else:
                if product in sales:
                    sales[product][0] += quantity
                    sales[product][1] = price
                else:
                    sales[product] = [quantity, price]

                print("Sales added successfully!")

        except ValueError:
            print("Enter valid numeric values.")

    elif choice == "2":
        if not sales:
            print("No sales data available.")
        else:
            print("\nProduct\tQuantity\tPrice\tRevenue")
            for product, details in sales.items():
                quantity, price = details
                print(product, "\t", quantity, "\t\t", price,
                      "\t", quantity * price)

    elif choice == "3":
        total = sum(quantity * price
                    for quantity, price in sales.values())
        print("Total Sales Revenue: ₹", round(total, 2))

    elif choice == "4":
        if not sales:
            print("No sales data available.")
        else:
            best = max(sales, key=lambda product: sales[product][0])
            print("Best-Selling Product:", best)
            print("Quantity Sold:", sales[best][0])

    elif choice == "5":
        print("Sales Data Analyzer closed.")
        break

    else:
        print("Invalid choice. Try again.")