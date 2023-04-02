import csv
import datetime

# define the name of the CSV file to store transaction information
filename = "transactions.csv"

# initialize an empty list to store transaction information
transactions = []

# define a function to record a new transaction
def record_transaction(description, amount, category):
    # get the current date and time
    timestamp = datetime.datetime.now()
    # create a dictionary to store the transaction details
    transaction = {"description": description, "amount": amount, "category": category, "timestamp": timestamp}
    # add the transaction to the transactions list
    transactions.append(transaction)
    # write the transaction to the CSV file
    write_to_csv(transaction)

# define a function to write transaction information to the CSV file
def write_to_csv(transaction):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([transaction['description'], transaction['amount'], transaction['category'], transaction['timestamp']])

# define a function to calculate profit
def calculate_profit():
    total_income = 0
    total_expense = 0
    for transaction in transactions:
        if transaction['amount'] > 0:
            total_income += transaction['amount']
        else:
            total_expense += abs(transaction['amount'])
    profit = total_income - total_expense
    print(f"Total income: ${total_income:.2f}")
    print(f"Total expense: ${total_expense:.2f}")
    print(f"Profit: ${profit:.2f}")

# define a function to print a summary of all transactions
def print_transactions():
    print("Transaction History:\n")
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                continue  # skip header row
            print(f"Transaction {i}:")
            print(f"Description: {row[0]}")
            print(f"Amount: ${float(row[1]):.2f}")
            print(f"Category: {row[2]}")
            print(f"Timestamp: {row[3]}\n")

# record some sample transactions
record_transaction("Salary", 2500.00, "Income")
record_transaction("Rent", -1000.00, "Expense")
record_transaction("Grocery shopping", -75.21, "Food")
record_transaction("Gas station", -35.00, "Transportation")
record_transaction("Movie tickets", -27.50, "Entertainment")

# calculate and print the profit
calculate_profit()

# print a summary of all transactions
print_transactions()
