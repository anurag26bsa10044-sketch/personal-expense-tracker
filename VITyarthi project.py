
#============================================
# PERSONAL EXPENSE & BUDGET TRACKER
# ============================================

expenses = []
budget = 0

# --------------------------------------------
# 1. ADD EXPENSE
# --------------------------------------------
def add_expense():
    print("\n========== ADD EXPENSE ==========")

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date (DD-MM-YYYY): ")

        if category == "" or description == "" or date == "":
            print("All fields are required.")
            return

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }

        expenses.append(expense)

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount. Please enter a number.")


# --------------------------------------------
# 2. VIEW EXPENSES
# --------------------------------------------
def view_expenses():
    print("\n========== ALL EXPENSES ==========")

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    total = 0

    for i in range(len(expenses)):
        expense = expenses[i]

        print("\nExpense", i + 1)
        print("Amount      :", "₹", expense["amount"])
        print("Category    :", expense["category"])
        print("Description :", expense["description"])
        print("Date        :", expense["date"])

        total = total + expense["amount"]

    print("\n----------------------------------")
    print("Total Expenses:", "₹", total)


# --------------------------------------------
# 3. SEARCH EXPENSES
# --------------------------------------------
def search_expenses():
    print("\n========== SEARCH EXPENSES ==========")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    category = input("Enter category to search: ")

    found = False
    total = 0

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            print("\nAmount      :", "₹", expense["amount"])
            print("Description :", expense["description"])
            print("Date        :", expense["date"])

            total = total + expense["amount"]
            found = True

    if found:
        print("\nTotal spent in", category, ":", "₹", total)
    else:
        print("No expenses found in this category.")


# --------------------------------------------
# 4. SET BUDGET
# --------------------------------------------
def set_budget():
    global budget

    print("\n========== SET BUDGET ==========")

    try:
        amount = float(input("Enter monthly budget: ₹"))

        if amount <= 0:
            print("Budget must be greater than 0.")
            return

        budget = amount

        print("Monthly budget set to ₹", budget)

    except ValueError:
        print("Invalid amount. Please enter a number.")


# --------------------------------------------
# 5. CHECK BUDGET
# --------------------------------------------
def check_budget():
    print("\n========== BUDGET STATUS ==========")

    if budget == 0:
        print("Please set your budget first.")
        return

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    remaining = budget - total

    print("Monthly Budget :", "₹", budget)
    print("Total Spent    :", "₹", total)
    print("Remaining      :", "₹", remaining)

    if total > budget:
        print("WARNING: You have exceeded your budget!")

    elif total >= budget * 0.8:
        print("WARNING: You have used more than 80% of your budget.")

    else:
        print("Status: You are within your budget.")


# --------------------------------------------
# 6. EXPENSE ANALYSIS
# --------------------------------------------
def expense_analysis():
    print("\n========== EXPENSE ANALYSIS ==========")

    if len(expenses) == 0:
        print("No expenses available for analysis.")
        return

    total = 0
    highest = expenses[0]["amount"]
    lowest = expenses[0]["amount"]

    highest_category = expenses[0]["category"]
    lowest_category = expenses[0]["category"]

    # Calculate total, highest and lowest
    for expense in expenses:

        amount = expense["amount"]

        total = total + amount

        if amount > highest:
            highest = amount
            highest_category = expense["category"]

        if amount < lowest:
            lowest = amount
            lowest_category = expense["category"]

    average = total / len(expenses)

    print("Total Expenses :", "₹", total)
    print("Average Expense:", "₹", round(average, 2))

    print("Highest Expense:", "₹", highest)
    print("Category       :", highest_category)

    print("Lowest Expense :", "₹", lowest)
    print("Category       :", lowest_category)


# --------------------------------------------
# 7. MONTHLY REPORT
# --------------------------------------------
def generate_report():
    print("\n======================================")
    print("          MONTHLY EXPENSE REPORT")
    print("======================================")

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Monthly Budget :", "₹", budget)
    print("Total Spent    :", "₹", total)

    if budget > 0:
        remaining = budget - total
        print("Remaining      :", "₹", remaining)

        if total > budget:
            print("Status         : Budget Exceeded")

        elif total >= budget * 0.8:
            print("Status         : Near Budget Limit")

        else:
            print("Status         : Within Budget")

    else:
        print("Status         : Budget Not Set")

    print("Number of Expenses:", len(expenses))

    print("======================================")


# --------------------------------------------
# 8. MAIN MENU
# --------------------------------------------
def main():

    while True:

        print("\n")
        print("==========================================")
        print("       PERSONAL EXPENSE & BUDGET TRACKER")
        print("==========================================")
        
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Set Budget")
        print("5. Check Budget")
        print("6. Expense Analysis")
        print("7. Generate Monthly Report")
        print("8. Exit")

        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expenses()

        elif choice == "4":
            set_budget()

        elif choice == "5":
            check_budget()

        elif choice == "6":
            expense_analysis()

        elif choice == "7":
            generate_report()

        elif choice == "8":
            print("\nThank you for using the Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1-8.")


# --------------------------------------------
# START PROGRAM
# --------------------------------------------

main()