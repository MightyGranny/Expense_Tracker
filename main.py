# This is our main list in which every expense will be stored
expenses = []

# A simple boolean variable to check whether user wants to edit or delete an expense or not.
modified = False 

# This user-defined function will ask user input of amount, category, and its description. This block returns expenses in dictionary form
def add_expense():
        
        # This is our dictionary where each input have its seperate place.
        expense = {}

        # This is the loop to ask as many input as user needed without any error.
        while True:

            # This try & except block is the main block for user input,
            try:
                amount = float(input("\nEnter amount of your Expence: "))
                category = input("What is the category of your Expence: ")
                description = input("Why this expense is commited: ")
                expense["amount"] = amount 
                expense["category"] = category
                expense["description"] = description
                break

            except ValueError:
                print("Invalid Amount!")
        return expense

# This block of code calculate the total expense CATEGORY WISE. And return the result in a very systematic way.
def total_category_expense(expenses):

    # This is the dictionary representition of our categories.
    category_total = {}
    # This loop here, seperates all the categories and calculate their total seperately. So that you know in which your money goes.
    for expend in expenses:

        # This here seperates the categories of Category of expense and amount of expense.
        category = expend["category"]
        amount = expend["amount"]
        # This calculates the total expense for each category.
        if category in category_total:
            # print(f"{category} is in dictionary")
            category_total[category] += amount

        else:
            # print(f"{category} is not in dictionary")
            category_total[category] = amount
    result = ""

    for category, total in category_total.items():
        result += f"{category} : {total}\n"

    return result


# This user-defined function calculates the total amount of expense according to the amount you have entered.
def total_expense(expenses):
    total = 0

    for expend in expenses:
        total += expend["amount"]

    return total


# This function displays the expenses for your convinience. In a proper manner, with every expense with its amount, category, and description.
def display_expenses(expenses):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EXPENCE TRACKER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    for index, expend in enumerate(expenses):

        print(f"\nExpense {index + 1}")
        print(f"Amount: ₹{expend['amount']}")
        print(f"Category: {expend['category']}")
        print(f"Description: {expend['description']}")


    print("-------------------------------------------------------------------------------")
    print("Your total expence is: ₹", total_expense(expenses), "\n")
    print(total_category_expense(expenses))


# This is our main loop of the Expense Tracker where all the functions are used
while True:

    further = input("\nDo you want to enter an expence (y/n): ").lower()

    if further == "y":
        expense = add_expense()
        expenses.append(expense)


    elif further == "n":
        break

    else:
        print("Invalid input! Please enter y or n.")


display_expenses(expenses)

# This loop asks user whether he/she wants to edit an expense or not
while True:
    ask_for_edit = input("Do you want to edit an expense (enter y for yes/n for no): ").lower()
    if ask_for_edit == "y":
        try:
            choice = int(input("Enter expense number to edit (or enter 0 to do nothing): "))
        except ValueError:
            print("Invalid Input!")
            continue

        if choice <= 0:
            print("Nothing to edit")
            break
        elif choice > len(expenses):
            print("Enter correct expense")
        else:
            while True:
                try:
                    expenses[choice - 1]["amount"] = float(input("\nEnter new amount of your Expence: "))
                    expenses[choice - 1]["category"] = input("What is the category of your Expence: ")
                    expenses[choice - 1]["description"] = input("Why this expense is commited: ")
                    modified = True
                    break
                except ValueError:
                    print("Invalid Input!")

                                    
    elif ask_for_edit == "n":
        print("You don't want to edit an expense")
        break   
    else:
        print("Invalid Input! Please enter y/n.")



# This loop asks user whether he/she wants to delete an expense or not
while True:
    ask_for_delete = input("Do you want to delete an expense (Please enter y for yes/n for no): ").lower()

    if ask_for_delete == "y":
        try:
            delete = int(input('\nEnter the expense number you want to delete (or enter 0 to do nothing): '))
        except ValueError:
            print("Invalid Input!")
            continue  
        try:
            if delete <= 0:
                print("Nothing to delete.")
                break
            elif delete > len(expenses):
                print("Enter correct expense number.")
            else:
                expenses.pop(delete-1)
                modified = True
                print(f"Expense {delete} deleted Successfully!")
            break
        except ValueError:
            print("Invalid Input!")
    elif ask_for_delete == "n":
        print("You don't want to delete an expense.\n")
        break
    else:
        print("Invalid Input! Please enter y/n.")


if not modified:
    print("\n\nThe earlier expeses are the only original expenses. There are no modification done.")
elif expenses == []:
    print("Nothing to Display. There is no data in Expense Tracker")
else:
    print("\nExpences updated successfully!\n")
    display_expenses(expenses)