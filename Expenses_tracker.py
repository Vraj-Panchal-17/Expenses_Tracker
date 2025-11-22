# Expense Tracker: Track daily expenses, categorize them, and show totals using lists and dictionaries. Save/read data from text files for persistence.​

expenses = []

def menu():
    print("\n---Daily Expenses---")
    print("1.Add Expenses") 
    print("2.View Expense") 
    print("3.Delete Expenses")
    print("4.Exit")

while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("1")
    if choice == 2:
        print("2")
    if choice == 3:
        print("3")
    if choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid input!, Try again.")

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

