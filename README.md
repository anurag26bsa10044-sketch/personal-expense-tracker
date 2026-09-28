# Personal Expense & Budget Tracker

## Project Title
**Personal Expense & Budget Tracker**

## Overview
The Personal Expense & Budget Tracker is a beginner-friendly, console-based Python application designed to help users record daily expenses, manage a monthly budget, and understand their spending.

The project uses core Python concepts such as functions, lists, dictionaries, loops, conditionals, and basic exception handling. It runs directly in the terminal and does not require external libraries, a database, or an internet connection.

## Features

### 1. Add Expense
- Enter expense amount, category, description, and date.
- The amount must be a positive number.
- The expense is stored in the program's in-memory expense list.

### 2. View Expenses
- Displays all recorded expenses in a numbered list.
- Shows the total amount spent.

### 3. Search Expenses
- Search expenses by category.
- Category search is case-insensitive.
- Displays matching expenses and the total spent in that category.

### 4. Set Monthly Budget
- Allows the user to enter a monthly budget.
- The budget must be a positive number.

### 5. Check Budget
- Compares total spending with the set budget.
- Shows the remaining balance.
- Gives a warning when spending reaches 80% or more of the budget.
- Shows an exceeded-budget status when spending goes beyond the budget.

### 6. Expense Analysis
- Calculates total spending.
- Calculates average expense.
- Identifies the highest and lowest expense.
- Shows the categories associated with the highest and lowest expenses.

### 7. Monthly Report
- Displays the budget.
- Displays total spending.
- Displays the remaining balance.
- Shows the budget status.
- Shows the total number of recorded expenses.

### 8. Exit
- Safely exits the menu-driven application.

## Technologies / Tools Used
- **Python 3**
- Python standard library only
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- `try/except` for basic input validation
- Terminal / Command Prompt
- GitHub for project submission and version control


## Installation & Run Instructions

### Step 1: Install Python
Install Python 3.x if it is not already installed.

### Step 2: Download or Clone the Repository
Download the project from GitHub or clone the repository using Git.

### Step 3: Open the Project Folder
Open Command Prompt / Terminal and move to the project folder.

Example:

```bash
cd Personal-Expense-Budget-Tracker
```

### Step 4: Run the Program

```bash
python expenditureVITyarthiproject.py
```

If your system uses `python3`, run:

```bash
python3 expenditureVITyarthiproject.py
```

### Step 5: Use the Menu
Choose the required numbered option from the menu. After completing an operation, the program returns to the main menu until the user selects Exit.

## Instructions for Testing

The project can be tested manually using valid and invalid inputs.

### Test 1: Add Expense
1. Select **Add Expense**.
2. Enter a positive amount.
3. Enter category, description, and date.
4. Confirm that the expense is added successfully.

### Test 2: Invalid Expense Amount
1. Select **Add Expense**.
2. Enter text instead of a number for the amount.
3. Confirm that the program displays an error instead of crashing.
4. Test a zero or negative amount and confirm that it is rejected.

### Test 3: View Expenses
1. Add one or more expenses.
2. Select **View Expenses**.
3. Confirm that all expenses and the total are displayed.

### Test 4: Search by Category
1. Add expenses under categories such as `Food` and `Travel`.
2. Search for `food` or `Food`.
3. Confirm that matching entries are displayed regardless of capitalization.

### Test 5: Budget Check
1. Set a positive monthly budget.
2. Add expenses below the budget.
3. Check the remaining balance.
4. Test spending at or above 80% of the budget.
5. Test spending above the budget and confirm the exceeded-budget warning.

### Test 6: Expense Analysis
1. Add multiple expenses with different amounts.
2. Select Expense Analysis.
3. Confirm that total, average, highest, lowest, and related categories are displayed.

### Test 7: Monthly Report
1. Set a budget and add expenses.
2. Generate the monthly report.
3. Confirm that budget, total spent, remaining balance, budget status, and expense count are shown.



## Author
**Anurag Prasad**
