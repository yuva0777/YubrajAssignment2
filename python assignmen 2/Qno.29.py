age = int(input("Enter your age: "))
degree = input("Do you have a degree? (yes/no): ").strip().lower()
experience = float(input("Enter your work experience in years: "))
if age >= 18:
    if degree == "yes":
        if experience > 3:
            print("Highly Eligible.")
        elif 1 <= experience <= 3:
            print("Eligible.")
        else:
            print("Under Review.")
    else:
        print("You need a degree to be considered for the job.")
else:
    print("Not eligible")
