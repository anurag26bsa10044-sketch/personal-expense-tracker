# Project Statement

## Project Title
**Personal Expense & Budget Tracker**

## 1. Problem Statement

Managing daily expenses can be difficult when small purchases such as food, travel, groceries, and subscriptions are not tracked regularly. Manual tracking on paper can be tedious and easy to forget, while full-featured finance applications may be more complex than a student or beginner needs.

The Personal Expense & Budget Tracker addresses this problem by providing a lightweight, menu-driven console application that allows a user to:

- Quickly record an expense when it occurs.
- View previously recorded expenses and the total amount spent.
- Search expenses by category such as Food, Travel, or Rent.
- Set a monthly budget and check whether spending is within the budget.
- Analyse spending and generate a simple monthly summary report.

The application is designed to provide these capabilities through a simple terminal-based interface without requiring a database, external libraries, or an internet connection.

## 2. Scope of the Project

The scope of the project is to create a beginner-level Python application for basic personal expense and budget management.

The project includes:

- Recording individual expenses.
- Storing expense amount, category, description, and date.
- Viewing all recorded expenses.
- Searching expenses by category.
- Setting a monthly budget.
- Checking spending against the budget.
- Calculating basic expense statistics.
- Generating a formatted monthly report.
- Validating numeric and text inputs.
- Providing a simple numbered console menu.

The current project uses in-memory data storage. Expenses and the budget are not intended to persist after the program is closed.

## 3. Target Users

The primary target users are:

- Students who want to track everyday spending.
- Beginners learning Python programming.
- Individuals who need a simple personal expense tracker.
- Users who prefer a lightweight terminal-based application.
- Users who need basic budget monitoring without a complex financial application.

## 4. High-Level Features

### Expense Management
- Add a new expense.
- Store amount, category, description, and date.
- Validate that expense amounts are positive.
- View all recorded expenses.
- Calculate total spending.
- Search expenses by category using case-insensitive matching.

### Budget Management
- Set a monthly budget.
- Validate that the budget is positive.
- Compare total expenses with the budget.
- Display the remaining budget.
- Warn the user when spending reaches 80% or more of the budget.
- Indicate when the budget has been exceeded.

### Analysis & Reporting
- Calculate total expenses.
- Calculate average expense.
- Identify the highest expense.
- Identify the lowest expense.
- Identify the categories of the highest and lowest expenses.
- Generate a monthly report containing budget, total spent, remaining balance, budget status, and number of expenses.

### Input Validation & Reliability
- Handle invalid numeric input using `try/except`.
- Prevent invalid or empty text fields where required.
- Keep the application running instead of crashing on common input errors.

## 5. Technical Scope

The project is implemented using Python 3 and standard Python features.

The main concepts used are:

- Functions for modularity.
- Lists for storing expenses.
- Dictionaries for representing individual expenses.
- Loops for menu operation and expense processing.
- Conditional statements for menu selection and budget status.
- `try/except` blocks for basic error handling.
- In-memory data storage.

No third-party libraries, external database, or internet connection is required.

## 6. Expected Outcome

The expected outcome is a simple and functional console application through which a user can record expenses, monitor a monthly budget, analyse spending, and generate a basic report.

The project also demonstrates how fundamental Python programming concepts can be combined to build a practical application.
