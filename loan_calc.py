
# Get loan details
money_owed = float(input("How much money do you owe?\n")) # 50,000
apr = float(input("What is the annual percentage rate?\n")) # 3%
payment = float(input("What will your monthly payment be in dollars?\n")) # $1000
months = int(input("How many months do you want to see results for?\n"))

# Divide by 100 to make percent then divide by 12 for monthly
monthly_rate = apr / 100 / 12

for i in range(months):
    # Add interst
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed, end = " ")
        print("You paid off the loan in", i + 1, "months")
        break
    # Make payment
    money_owed = money_owed - payment

    # Print reults after this month

    print("Paid", payment, "of which", interest_paid, "was interest", end = ' ')
    print("Now I owe", money_owed)
