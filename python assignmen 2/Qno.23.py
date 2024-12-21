age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
days = int(input("Enter the number of days worked: "))
if 18 <= age < 30:
    if gender == 'M':
        wage_per_day = 700
    elif gender == 'F':
        wage_per_day = 750
    else:
        wage_per_day = 0  
elif 30 <= age <= 40:
    if gender == 'M':
        wage_per_day = 800
    elif gender == 'F':
        wage_per_day = 850
    else:
        wage_per_day = 0 
else:
  wage_per_day = 0
if wage_per_day > 0:
    total_wages = wage_per_day * days
    print(f"The total wages are: {total_wages}")
else:
    print("Invalid age or gender!")
