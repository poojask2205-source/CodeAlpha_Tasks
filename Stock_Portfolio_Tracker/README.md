# TASK 2 : Stock Portfolio Tracker 📈

## Description

Stock Portfolio Tracker is a simple Python desktop application that helps users manage their stock investments. The user can select a stock, enter the quantity, and the application calculates the investment amount automatically.

The project uses a small list of predefined stocks with fixed prices. Users can add multiple stocks, view their portfolio, check the total investment, and save the portfolio details to a text file.

## Features

* Select stocks from a dropdown list
* Enter the quantity of stocks
* Calculate investment automatically
* Display portfolio details in a table
* Show total investment
* Save portfolio to a `.txt` file
* Clear the portfolio
* Simple and user-friendly desktop interface

## Available Stocks

The application contains 5 predefined stocks:

* **AAPL** – $180
* **TSLA** – $250
* **GOOGL** – $150
* **AMZN** – $200
* **MSFT** – $420

## How It Works

The investment is calculated using:

```text
Investment = Stock Price × Quantity
```

For example, if the user selects AAPL and enters 5 shares:

```text
$180 × 5 = $900
```

The investment amount is then added to the total portfolio value.

## Technologies Used

* Python
* Tkinter
* ttk
* datetime
* File Handling

## Key Concepts

* Dictionary
* Lists
* Functions
* Input and Output
* Basic Arithmetic
* If-else Conditions
* Exception Handling
* File Handling
* GUI Programming

## How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python tracker.py
```

## Output File

When the **Save Portfolio** button is clicked, the application saves the portfolio information in:

```text
stock_investment.txt
```

The file contains the stock name, quantity, price, investment amount, date, and total investment.



## Result

The Stock Portfolio Tracker successfully calculates and displays the total investment based on the selected stocks and quantities. It also allows the user to save the portfolio details for future reference.
