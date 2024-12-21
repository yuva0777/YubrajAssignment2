income = float(input("Enter your income: "))
credit = int(input("Enter your credit score: "))
if income > 50000:
    if credit > 700:
        print("Loan Approved.")
    elif 600 <= credit <= 700:
        print("Loan Approved with a higher interest rate.")
    else:
        print("Loan Rejected due to low credit score.")
else:
    print("Loan Rejected")
