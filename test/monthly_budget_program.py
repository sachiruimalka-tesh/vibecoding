# Monthly Budget Program

# Ask for total monthly budget
budget = float(input("Enter your total monthly budget (LKR): "))

total_expense = 0

# Allow user to enter expenses multiple times
while True:
    expense = input("Enter an expense (or type 'done' to stop): ")

    if expense.lower() == "done":
        break

    total_expense = total_expense + float(expense)

# Calculate remaining balance
balance = budget - total_expense

# Display results
print("------------------------------")
print("Total Budget       :", budget, "LKR")
print("Total Expenses     :", total_expense, "LKR")
print("Remaining Balance  :", balance, "LKR")

# Warning message
if balance < 500:
    print("Warning: Low Funds")

print("------------------------------")
