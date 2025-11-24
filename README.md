# -25BAI11304-Expense-Tracker
Vityarthi project on an Expense Tracker 
Expense Tracker (Python CLI)
This is a simple command-line interface application for tracking personal expenses; it's entirely written in Python. It allows users to add, view, summarize, and delete expense records.
Setup and Usage
Requirements
This application requires Python 3.
Installation
1. Clone repository:
git clone https://github.com/voilentpiggy13/-25BAI11304-Expense-Tracker/tree/main
name- Expense Tracker

3.	Execute the script:
python vithyarthi project.py



Running the Application

Once run, the application will present the following main menu:
EXPENSE TRACKER
 1. Add a new expense
 2. View all expenses 
3. View total amount spent 
4. View total spent by category 
5. Delete an expense
0. Exit Your choice:
Type the number corresponding to your desired action (1-5 or 0 to quit).

Technical Documentation: Code Details
Global State Variables
The data of the application is kept in memory by two global variables:


•	expenseData: A list that holds all expense records. Each expense record is a dictionary.


•	Next ID: An integer that keeps track of the ID for the next expense added so that each expense added gets a unique identifier.
expenseData = []
nextId = 1
Core Functions
Function	Purpose	Details
show_menu()	Display Menu	Prints the main menu options to the console.
add_new_expense()	Add Expense	Prompts the user for date, category, description, and amount. Creates a new dictionary entry, assigns it nextId, appends it to expenseData, and increments nextId. Includes basic error handling for non-numeric amounts.
view_all()	View Expenses	Iterates through expenseData and prints all records in a formatted, table-like structure. It truncates the description if it exceeds 18 characters for cleaner formatting.
total_spent()	Calculate Total	Iterates through expenseData and sums the amount of all entries to display the grand total spent.
total_by_cat()	Category Summary	Uses a dictionary (totals) to aggregate amounts. It iterates through expenses, using the expense category as the key and accumulating the total amount spent for that category.
find_expense(theId)	Helper Search	Iterates through expenseData to find and return the expense dictionary whose id matches the input theId. Returns None if no match is found.
delete_expense()	Delete Expense	Prompts for an ID, validates the input, uses find_expense to locate the record, asks for confirmation, and removes the dictionary from expenseData.

Main Program Loop
The application runs in an infinite while True loop, guaranteeing that the program will keep running until the user consciously chooses option 0 (Exit).
1. Calls show_menu().


2. Takes user input for the choice.
3. Utilizes an if/elif/else block to invoke the respective function depending on what the user entered.
4. The loop is exited by the break statement when choice == "0". 


Data Structure Expense records are stored as Python dictionaries, each with the following keys:
Key	Type	Description
"id"	int	Unique identifier for the expense.
"date"	str	Date of the expense (format: DD-MM-YYYY).
"category"	str	Category of the expense (e.g., Food, Travel, Bills).
"description"	str	A brief description of the expense.
"amount"	float	The monetary value of the expense.
Example Entry:
{
    "id": 1,
    "date": "25-11-2025",
    "category": "Food",
    "description": "Lunch with team",
    "amount": 15.50
}



