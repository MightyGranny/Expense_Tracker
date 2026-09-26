# 💰 Expense Tracker

A simple **command-line Expense Tracker built with Python** that allows users to record, view, edit, delete, and analyze their daily expenses.

This project was created to practice core Python programming concepts such as **lists, dictionaries, functions, loops, conditional statements, exception handling, input validation, and basic program structure**.

---

## 📌 Features

* ➕ **Add Expenses**

  * Enter the expense amount
  * Specify a category
  * Add a description

* 📋 **Display Expenses**

  * View all recorded expenses
  * See the amount, category, and description of each expense

* ✏️ **Edit Expenses**

  * Select an existing expense
  * Modify its details

* 🗑️ **Delete Expenses**

  * Remove an expense from the tracker

* 📊 **Expense Analysis**

  * Calculate the total amount spent
  * Calculate spending totals by category

* 🛡️ **Input Validation**

  * Handles invalid numerical input
  * Handles invalid menu choices
  * Handles invalid yes/no responses

* 🔄 **Continuous Menu**

  * The program returns to the main menu after completing an operation
  * The user can exit whenever they choose

---

## 🛠️ Technologies Used

* **Python 3**
* No external libraries are required

---

## 🧠 Python Concepts Practiced

This project focuses on several fundamental Python concepts:

```text
Variables
Lists
Dictionaries
Functions
Loops
Conditional Statements
String Formatting
Exception Handling
Input Validation
List Indexing
```

The expenses are stored using a **list of dictionaries**.

Example:

```python
expenses = [
    {
        "amount": 240.0,
        "category": "Travel",
        "description": "Bus fare"
    },
    {
        "amount": 45.0,
        "category": "Food",
        "description": "Lunch"
    }
]
```

---

## 📂 Project Structure

```text
Expense-Tracker/
│
├── main.py
└── README.md
```

### `main.py`

Contains the complete Expense Tracker program, including:

* Expense creation
* Expense display
* Expense editing
* Expense deletion
* Total expense calculation
* Category-wise expense calculation
* Input validation
* Main program loop

---

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

You can check your Python version with:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <your-repository-url>
```

### 3. Navigate to the Project

```bash
cd Expense-Tracker
```

### 4. Run the Program

```bash
python main.py
```

---

## 🖥️ How It Works

When the program starts, it displays a menu similar to:

```text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EXPENSE TRACKER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Add an Expense
2. Display Expenses
3. Edit an Expense
4. Delete an Expense
5. Exit
```

The user selects an operation by entering the corresponding number.

### Adding an Expense

The program asks for:

```text
Amount
Category
Description
```

The information is then stored in the `expenses` list.

### Viewing Expenses

The program displays all currently stored expenses and their details.

### Editing an Expense

The user selects an expense by its number and can modify its information.

### Deleting an Expense

The user selects an expense and removes it from the list.

### Expense Analysis

The program can calculate:

* Total amount spent
* Total spending for each category

For example:

```text
Travel : ₹240.0
Food   : ₹45.0

Total Expense : ₹285.0
```

---

## ⚠️ Current Limitations

This project currently stores expenses **only while the program is running**.

When the program is closed, the data is lost because it is stored in memory rather than a permanent database or file.

Other possible improvements include:

* Persistent data storage
* CSV/JSON support
* SQLite database
* Monthly expense reports
* Budget limits
* Graphical user interface
* Expense search and filtering
* Date and time tracking

---

## 🚀 Future Improvements

Possible future versions of this project could evolve from a simple command-line application into a more complete expense management system.

### Version 2

* Add dates to expenses
* Store data in JSON or CSV
* Search expenses
* Filter expenses by category

### Version 3

* Add SQLite database
* Add monthly/yearly reports
* Add budget tracking
* Add spending summaries

### Version 4

* Build a graphical interface
* Add charts and visualizations
* Create a web version using Flask

---

## 🎯 Project Goal

The main goal
