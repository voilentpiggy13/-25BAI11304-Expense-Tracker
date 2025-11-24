# -25BAI11304-Expense-Tracker
Vityarthi project on an Expense Tracker 
Project Report
By - (25BAI11304) Pratham Kumar Yadav

1. Problem Definition & Justification
This project addresses the basic problem of people not being able to track or summarize daily financial expenditures. Without a system, people lose track of where their money is going; hence, budgeting and planning are quite difficult.

Real-World Need: It should be a simple, easily accessible tool to record transactions digitally.

Target User: Anyone looking to get a simple, not cloud-based means of budgeting.

Justification: The project provides an efficient, digital alternative to manual paper-based logging. It offers immediate summaries by category and total amount.

2. Project Objectives and Expected Outcomes

The primary goal in this project was to develop a completely functional console-based application for managing expense information.

Objectives

Data Management: Design a structured format to store records of expenses using lists and dictionaries.

Perform CRUD Operations: Implement basic Create, Read, and Delete functionality.

Reporting: Provide basic financial reports such as Total Spent and Total Spent by Category.

Robustness: Provide basic input validation, such as an amount being a valid number.

User Experience: Design a simple, user-friendly, menu-driven interface.
Outcome	Achievement Status
New Entry Creation	Achieved (add_new_expense function)
Complete List Viewing	Achieved (view_all function)
Total Summation	Achieved (total_spent function)
Categorical Aggregation	Achieved (total_by_cat function)
Secure Deletion	Achieved (delete_expense function with confirmation)


3. Structured Development Process

The project followed a standard structured development process, applying course concepts like modular programming and data abstraction.
3.1 Requirement Analysis
Requirement	Implementation Detail
Store multiple expenses	Global list (expenseData) used as the database.
Each expense must have details	Python dictionary used for each expense record (ID, Date, Category, Description, Amount).
Unique identifier	Global integer counter (nextId) handles automatic, incremental ID assignment.
User interaction	input() and print() within a main loop.


3.2. Top-Down Design / Modularization

The solution was designed using Top-Down Design, breaking the overall application into specialized functions:
Module/Function	Concept Applied	Purpose
show_menu()	I/O, Modularity	Handles the presentation of options.
add_new_expense()	Data Abstraction, I/O, Error Handling	Encapsulates input, validation (try/except), and data saving logic.
total_by_cat()	Data Structures, Algorithm	Uses a dictionary (totals) for efficient counting/aggregation.
find_expense()	Search Algorithm	Implements a simple linear search to find records by ID.
while True loop	Control Flow	Manages the continuous running of the program until exit.


4. Algorithm Development and Implementation

4.1. Expense Aggregation Algorithm (total_by_cat)

The central problem when reporting was summarizing amounts by a non-unique field, Category. The solution will follow a Hash Map approach - Python dictionary:

Initialize an empty dictionary: totals = {}.

Iterate over every expense e in expenseData.

.cat of the current expense:

IF cat is not in totals: totals[cat] = 0

THEN Add the expense amount to the category's total: totals[cat] += e["amount"].

Print the resulting key-value pairs.

4.2. Tools and Programming Techniques

Language: Python 3.x

Data Structures: List (expenseData); Dictionary (for records and category totals)

Techniques:

Global Variables: Used for persistent state - expenseData and nextId.

5. Testing and Refinement
The final stage involved testing the core functionality and refining the user experience.
5.1. Test Cases
Feature Tested	Input	Expected Result	Actual Result
Adding Expense	Category: Food, Amount: 10.50	Expense with id=1 is added.	Pass
Viewing Total	(After adding 10.50 and 20.00)	Total: 30.50	Pass
Total by Category	Food: 10.50, Travel: 20.00	Food: 10.50, Travel: 20.00	Pass
Invalid Amount	Amount: "ten dollars"	Prints error message, entry is not saved.	Pass
Deletion	ID: 1, Confirmation: y	Expense 1 is removed from expenseData.	Pass

This Expense Tracker Python application is a great foundation for a project report. Based on the requirements you provided, here is a structured Project Report suitable for a course, focusing on the design and development process.
________________________________________
 Project Report: Simple Console Expense Tracker
1. Problem Definition & Justification
The core problem addressed by this project is the difficulty individuals face in tracking and summarizing their daily financial expenditures. Without a system, people often lose sight of where their money is going, making budgeting and financial planning challenging.
•	Real-world Need: A simple, readily available tool is needed to digitally log transactions.
•	Target User: Any individual or small group requiring a basic, non-cloud-based method to monitor spending.
•	Justification: The project provides an efficient, digital alternative to manual paper-based logging, offering instant summaries by category and total amount.
________________________________________
2. Project Objectives and Expected Outcomes
The primary goal was to develop a fully functional, console-based application that manages expense data.
 Objectives
1.	Data Management: Create a structured way to store expense records (using lists and dictionaries).
2.	CRUD Operations: Implement basic Create (Add), Read (View), and Delete functionality.
3.	Reporting: Provide basic financial reports (Total Spent and Total Spent by Category).
4.	Robustness: Implement basic input validation (e.g., checking if the amount is a valid number).
5.	User Experience: Create a simple, intuitive, and menu-driven interface.
 Expected Outcomes
Outcome	Achievement Status
New Entry Creation	Achieved (add_new_expense function)
Complete List Viewing	Achieved (view_all function)
Total Summation	Achieved (total_spent function)
Categorical Aggregation	Achieved (total_by_cat function)
Secure Deletion	Achieved (delete_expense function with confirmation)
________________________________________
3. Structured Development Process
The project followed a standard structured development process, applying course concepts like modular programming and data abstraction.
3.1. Requirement Analysis
Requirement	Implementation Detail
Store multiple expenses	Global list (expenseData) used as the database.
Each expense must have details	Python dictionary used for each expense record (ID, Date, Category, Description, Amount).
Unique identifier	Global integer counter (nextId) handles automatic, incremental ID assignment.
User interaction	input() and print() within a main loop.
3.2. Top-Down Design / Modularization
The solution was designed using Top-Down Design, breaking the overall application into specialized functions (modules):
Module/Function	Concept Applied	Purpose
show_menu()	I/O, Modularity	Handles the presentation of options.
add_new_expense()	Data Abstraction, I/O, Error Handling	Encapsulates input, validation (try/except), and data saving logic.
total_by_cat()	Data Structures, Algorithm	Uses a dictionary (totals) for efficient counting/aggregation.
find_expense()	Search Algorithm	Implements a simple linear search to find records by ID.
while True loop	Control Flow	Manages the continuous running of the program until exit.
________________________________________
4. Algorithm Development and Implementation
4.1. Expense Aggregation Algorithm (total_by_cat)
The core challenge in reporting was summarizing amounts by a non-unique field (Category). The solution uses a Hash Map approach (Python dictionary):
1.	Initialize an empty dictionary: totals = {}.
2.	Iterate through every expense e in expenseData.
3.	For the current expense's category (cat):
o	IF cat is not in totals: Initialize totals[cat] = 0.
o	THEN Add the expense amount to the category's total: totals[cat] += e["amount"].
4.	Print the resulting key-value pairs.
4.2. Tools and Programming Techniques
•	Language: Python 3.x
•	Data Structures: List (expenseData) and Dictionary (for records and category totals).
•	Techniques:
o	Global Variables: Used for persistent state (expenseData and nextId).
o	String Formatting: The view_all function uses f-string formatting (e.g., f'{e["amount"]:>8.2f}') for neat, aligned columnar output.
o	Input Validation: try...except ValueError is used in both add_new_expense and delete_expense to safely convert user input to float or int.
________________________________________
5. Testing and Refinement
The final stage involved testing the core functionality and refining the user experience.
5.1. Test Cases
Feature Tested	Input	Expected Result	Actual Result
Adding Expense	Category: Food, Amount: 10.50	Expense with id=1 is added.	Pass
Viewing Total	(After adding 10.50 and 20.00)	Total: 30.50	Pass
Total by Category	Food: 10.50, Travel: 20.00	Food: 10.50, Travel: 20.00	Pass
Invalid Amount	Amount: "ten dollars"	Prints error message, entry is not saved.	Pass
Deletion	ID: 1, Confirmation: y	Expense 1 is removed from expenseData.	Pass

5.2. Refinement
•	Confirmation Prompt: Added the "Are you SURE? (y/n)" prompt in delete_expense to prevent accidental data loss.
•	Description Truncation: The view_all function was refined to truncate long descriptions with "..." to ensure the table format remains clean and readable.
This project successfully implemented the required expense tracking features, demonstrating modular design, appropriate data structure selection, and robust input handling.


