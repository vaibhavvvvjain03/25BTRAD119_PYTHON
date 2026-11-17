class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Withdrawal successful!")

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance: ₹", self.__balance)


account = BankAccount("Vaibhav", 1000)

while True:
    print("\n1.Deposit  2.Withdraw  3.Balance  4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        account.deposit(float(input("Enter amount: ")))
    elif choice == "2":
        account.withdraw(float(input("Enter amount: ")))
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")