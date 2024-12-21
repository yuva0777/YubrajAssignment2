percentage = float(input("Enter your percentage: "))
if percentage < 40:
    print("Category: Failed")
elif 40 <= percentage < 55:
    print("Category: Fair")
elif 55 <= percentage < 65:
    print("Category: Good")
elif percentage >= 65:
    print("Category: Excellent")
else:
    print("Invalid percentage entered!")
