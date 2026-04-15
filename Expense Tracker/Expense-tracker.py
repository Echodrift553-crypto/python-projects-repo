import json

user_expenses = []

def load_expenses():
    global user_expenses
    try:
        with open("expenses.json", "r") as file:
            user_expenses = json.load(file)
            if not isinstance(user_expenses, list):
                user_expenses = []
    except (FileNotFoundError, json.JSONDecodeError):
        user_expenses = []


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(user_expenses, file, indent=4)


def del_expense():
    if ( len(user_expenses) == 0 ):
        print("No expense to delete!")
        return
    
    show_expense()

    try:
        del_index = int(input("enter the index to delete"))
        if ( del_index < 0 or del_index >= len(user_expenses)):
            print("INVALID INDEX")
            return
        
        user_expenses.pop(del_index)
        print('Expense deleted successfully!')
        save_expenses()

    except ValueError:
        print("Enter a Valid Number")

def highest_expense():
    highest = 0 
    for expense in user_expenses:
        if ( expense.get('Amount') > highest):
            highest = expense.get('Amount')
    
    print(f"Highest expense is : {highest}")
    
    print(f"\nDATE : {expense.get('Date')}")
    print(f"CATEGORY : {expense.get('Category')}")
    print(f"AMOUNT : {expense.get('Amount')}")
    print(f"DESCRIPTION : {expense.get('Description')}")


def search_by_date():
    date = input("Enter the date of expense (DD-MM-YYYY): ")
    for expense in user_expenses:
        if ( expense.get('Date') == date):
            print(f"\nDATE : {expense.get('Date')}")
            print(f"CATEGORY : {expense.get('Category')}")
            print(f"AMOUNT : {expense.get('Amount')}")
            print(f"DESCRIPTION : {expense.get('Description')}")


def filter_expense():
    if ( len(user_expenses) == 0 ):
        print("NO expense to filter")
        return

    try:
        category_filter = input("enter the category of expense: ").lower()

        for expense in user_expenses:
            if ( expense.get('Category') == category_filter):
                print(f"\nDATE : {expense.get('Date')}")
                print(f"CATEGORY : {expense.get('Category')}")
                print(f"AMOUNT : {expense.get('Amount')}")
                print(f"DESCRIPTION : {expense.get('Description')}")

    except ValueError:
        print("enter a valid category!")
     

def add_expense():
    date = input("Enter the date of expense (DD-MM-YYYY): ")
    category = input("Enter the category of the expense: ").lower()

    try:
        amount = float(input("Enter the amount of expense: "))
    except ValueError:
        print("INVALID INPUT")
        return
    
    description = input("Enter the description of expense: ").lower()

    expense = {
        "Date" : date,
        "Category" : category,
        "Amount" : amount,
        "Description" : description
    }

    user_expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")


def show_expense():
    if ( len(user_expenses) == 0 ):
        print("No expense found to show. Please add expense first!")
        return
    
    for expense in user_expenses:
        print(f"\nDATE : {expense.get('Date')}")
        print(f"CATEGORY : {expense.get('Category')}")
        print(f"AMOUNT : {expense.get('Amount')}")
        print(f"DESCRIPTION : {expense.get('Description')}")
        

def total_expense():
    total = 0
    for expense in user_expenses:
        total += expense.get("Amount")
    print(f"The total expense is : {total}")
    

def main():
    load_expenses()
    while True:
        print('''Choose your operation below:
            1. Add expense
            2. Show expense
            3. Show total expense
            4. Exit the program
            5. Delete expense
            6. filter expense by category
            7. filter expense by highest expense
            8. Show highest expense''')
        try:
            user_choice = int(input("Select the required operation: "))
        except ValueError:
            print("Please enter a number!")
            continue
        
        if ( user_choice == 1 ):
            add_expense()

        elif ( user_choice == 2 ):
            show_expense()

        elif ( user_choice == 3 ):
            total_expense()

        elif ( user_choice == 4 ):
            print("THANK-YOU FOR USING THE SERVICE")
            break

        elif( user_choice == 5 ):
            del_expense()

        elif( user_choice == 6 ):
            filter_expense()

        elif( user_choice == 7):
            search_by_date()
            
        elif ( user_choice == 8):
            highest_expense()

        else:
            print("INVALID INPUT! PLEASE ENTER NUMEBR FROM 1 TO 4")


main()