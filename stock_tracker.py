
# Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

# Store user investments
portfolio = {}

total_investment = 0

print("======================================")
print("       STOCK PORTFOLIO TRACKER")
print("======================================")

print("\nAvailable Stocks and Prices:")

for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

print("\nEnter your stock investments.")
print("Type 'done' when finished.\n")

# User input loop
while True:

    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    # Check whether stock exists
    if stock_name not in stock_prices:
        print("Stock not available! Please try again.")
        continue

    # Enter quantity
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            continue

    except ValueError:
        print("Please enter a valid number!")
        continue

    # Calculate investment
    investment = stock_prices[stock_name] * quantity

    # Store investment
    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

    total_investment += investment

    print("Investment added successfully!")
    print("Value: $", investment)

# Display portfolio
print("\n======================================")
print("          YOUR PORTFOLIO")
print("======================================")

if portfolio:

    print("\nStock\tQuantity\tPrice\tInvestment")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        investment = price * quantity

        print(stock, "\t", quantity, "\t\t$", price,
              "\t$", investment)

    print("\nTotal Investment: $", total_investment)

    # Save portfolio to text file
    with open("portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO TRACKER\n")
        file.write("======================\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            investment = price * quantity

            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: ${price} | Investment: ${investment}\n"
            )

        file.write("\nTotal Investment: $" + str(total_investment))

    print("\nPortfolio saved successfully in portfolio.txt")

else:
    print("\nNo stocks were added to your portfolio.")

print("\nThank you for using Stock Portfolio Tracker!")
