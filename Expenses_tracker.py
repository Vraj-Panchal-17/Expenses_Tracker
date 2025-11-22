# Expense Tracker: A simple program to add, view, delete and store expenses in a text file.

expenses = [] # List to store all expenses in memory

def menu():
    print("\n---Daily Expenses---")
    print("1.Add Expenses") 
    print("2.View Expense") 
    print("3.Delete Expenses")
    print("4.Exit")

# Loading old expenses from file when program starts
try:
    with open("total_expenses.txt", "r") as f:
        data = f.read().strip()

        # Only process if file is not empty
        if data:
            for line in data.split("\n"):
                amount, category, description = line.split("|")

                # Store each expense as a dictionary
                expenses.append({
                    "amount": float(amount),
                    "category": category,
                    "description": description
                })
except FileNotFoundError:
    # Create file if it doesn't exist
    with open("total_expenses.txt", "w") as f:
        pass

def add_expenses():
    # Taking user input for a new expense
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")  

    # Adding expense to list
    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })

    # Also saving it to file for future use
    with open("total_expenses.txt", "a") as f:
        f.write(f"{amount}|{category}|{description}\n")
    
    print("Expenses added successfully.")

def view_expenses():
    # If no expenses exist
    if len(expenses) == 0:
        print("Daily Expenses list is empty.")
        return
    
    # Show all expenses with numbering
    idx = 1
    for exp in expenses:
        print(f"{idx}.₹{exp['amount']} - {exp['category']} - {exp['description']}")
        idx += 1


def delete_expenses():
    # If list is empty
    if len(expenses) == 0:
        print("Daily Expenses list is empty.")
        return

    # Show current expenses before deleting
    view_expenses()

    choice = int(input("Enter the expenses number to remove: "))

    idx = choice - 1

    # Validate user choic
    if idx < 0 or idx >=len(expenses):
        print("Invalid Choice.")

    # Delete the selected expense from list
    expenses.pop(idx)
    print("Expenses delete successfully.")

    # Rewrite the updated list back into the file
    with open("total_expenses.txt", "w") as f:
        for exp in expenses:
            f.write(f"{exp['amount']}|{exp['category']}|{exp['description']}\n") 

while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_expenses()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        delete_expenses()
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid input!, Try again.")