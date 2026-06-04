# Expense Tracker

expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spent")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter expense amount: ₹"))
            expenses.append(amount)
            print("Expense added successfully!")
        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. ₹{expense}")

    elif choice == "3":
        total = sum(expenses)
        print(f"\nTotal Spent: ₹{total}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")