# Expense Tracker: Track daily expenses, categorize them, and show totals using lists and dictionaries. Save/read data from text files for persistence.​

expenses = []

def menu():
    print("\n---Daily Expenses---")
    print("1.Add Expenses") 
    print("2.View Expense") 
    print("3.Delete Expenses")
    print("4.Exit")


with open("total_expenses.txt", "r") as f:
    data = f.read().strip()
    if data:
        for line in data.split("\n"):
            amount, category, description = line.split("|")
            expenses.append({
                "amount": float(amount),
                "category": category,
                "description": description
            })

def add_expenses():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")  

    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })

    with open("total_expenses.txt", "a") as f:
        f.write(f"{amount}|{category}|{description}\n")
    
    print("Expenses added successfully.")

def view_expenses():
    if len(expenses) == 0:
        print("Daily Expenses list is empty.")
        return
    
    idx = 1
    for exp in expenses:
        print(f"{idx}.₹{exp['amount']} - {exp['category']} - {exp['description']}")
        idx += 1


def delete_expenses():
    if len(expenses) == 0:
        print("Daily Expenses list is empty.")
        return

    view_expenses()

    choice = int(input("Enter the expenses number to remove: "))

    idx = choice - 1

    if idx <= 0 or idx >=len(expenses):
        print("Invalid Choice.")

    expenses.pop(idx)
    print("Expenses delete successfully.")

    with open("total_expenses.txt", "r") as f:
        for exp in expenses:
            f.write(f"{exp[amount]}|{exp[category]}|{exp[description]}\n")  

while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pass
    if choice == 2:
        pass
    if choice == 3:
        pass
    if choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid input!, Try again.")