# 📈 Stock Portfolio Tracker Using Python

## 📌 Project Overview

The **Stock Portfolio Tracker** is a simple Python-based application that allows users to track their stock investments and calculate the total investment value.

Users can enter stock symbols and quantities. The application uses a predefined dictionary of stock prices to calculate individual stock investments and the overall portfolio value.

The portfolio details are also automatically saved in a `portfolio.txt` file.

## 🎯 Project Objectives

- Build a simple stock portfolio tracking application.
- Store stock prices using a Python dictionary.
- Accept stock names and quantities from users.
- Calculate individual and total investment values.
- Display a portfolio summary.
- Save investment details in a text file.

## ✨ Features

- Predefined stock prices.
- User input for stock symbols.
- User input for stock quantities.
- Automatic investment calculation.
- Support for multiple stock entries.
- Combines quantities when the same stock is entered multiple times.
- Validates stock names and quantities.
- Displays total portfolio investment.
- Automatically saves portfolio details in `portfolio.txt`.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Module:** None (uses Python built-in features)
- **Concepts:** Dictionary, Input/Output, Loops, Conditional Statements, Exception Handling, Basic Arithmetic, File Handling.

## 📊 Available Stocks and Prices

The application uses the following predefined stock prices:

| Stock Symbol | Stock Price |
|---|---:|
| AAPL | $180 |
| TSLA | $250 |
| GOOGL | $150 |
| MSFT | $420 |
| AMZN | $190 |

**Note:** These are manually defined example prices, not real-time stock market prices.

## 💡 How It Works

1. The application displays available stock symbols and prices.
2. The user enters a stock symbol.
3. The user enters the quantity of shares.
4. The program checks whether the stock symbol is valid.
5. The investment value is calculated using:

   **Investment = Stock Price × Quantity**

6. Users can enter multiple stocks.
7. Type `done` to finish entering investments.
8. The application displays the complete portfolio and total investment.
9. Portfolio details are saved automatically in `portfolio.txt`.

## 📂 Project Structure


Stock-Portfolio-Tracker/
│
├── stock_tracker.py
├── portfolio.txt
└── README.md


**Note:** The `portfolio.txt` file is automatically generated when the user adds at least one stock.

## ⚙️ Requirements

- Python 3.x
- Visual Studio Code (recommended)
- No external Python libraries required.

## 🚀 How to Run the Project

**Step 1:** Download or clone the project repository.

**Step 2:** Open the project folder in Visual Studio Code.

**Step 3:** Open the integrated terminal.

**Step 4:** Execute the following command:

**bash**
python stock_tracker.py


**Step 5:** Enter stock symbols and quantities.

**Step 6:** Type `done` to calculate and display your portfolio.

## 🖥️ Sample Output


======================================
       STOCK PORTFOLIO TRACKER
======================================

Available Stocks and Prices:
AAPL : $ 180
TSLA : $ 250
GOOGL : $ 150
MSFT : $ 420
AMZN : $ 190

Enter your stock investments.
Type 'done' when finished.

Enter stock name: AAPL
Enter quantity: 5
Investment added successfully!
Value: $ 900

Enter stock name: TSLA
Enter quantity: 2
Investment added successfully!
Value: $ 500

Enter stock name: done

======================================
          YOUR PORTFOLIO
======================================

Stock   Quantity   Price   Investment
AAPL       5        $180      $900
TSLA       2        $250      $500

Total Investment: $ 1400

Portfolio saved successfully in portfolio.txt

Thank you for using Stock Portfolio Tracker!


## 📁 Generated portfolio.txt File

After successful execution, the application generates a text file containing the portfolio details.

Example:


STOCK PORTFOLIO TRACKER
======================
AAPL | Quantity: 5 | Price: $180 | Investment: $900
TSLA | Quantity: 2 | Price: $250 | Investment: $500

Total Investment: $1400


## 📚 Key Python Concepts Used

| Concept | Description |
|---|---|
| Dictionary | Stores stock symbols and prices |
| Variables | Stores portfolio and investment values |
| Input() | Accepts user input |
| While Loop | Allows multiple stock entries |
| For Loop | Displays portfolio details |
| If-Else | Validates stock symbols |
| Try-Except | Handles invalid quantity input |
| Arithmetic Operators | Calculates investment values |
| File Handling | Saves portfolio in a text file |

## 🎓 Learning Outcomes

By completing this project, I learned how to:

- Work with Python dictionaries.
- Accept and process user input.
- Use loops and conditional statements.
- Perform basic financial calculations.
- Handle invalid user inputs using exception handling.
- Read and write files using Python.
- Build a simple real-world command-line application.

## 🔮 Future Enhancements

- Add real-time stock market prices using an API.
- Add more stock symbols.
- Create a graphical user interface (GUI).
- Export portfolio details to CSV or Excel.
- Add profit and loss calculations.
- Add portfolio performance charts.

⭐ If you find this project useful, feel free to star the repository!
