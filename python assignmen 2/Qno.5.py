sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
total_marks = sub1 + sub2 + sub3 + sub4
percentage = (total_marks / 400) * 100
if percentage > 70:
  print("distinction")
elif percentage > 60:
  print("First")
elif percentage > 40:
  print("pass")
else:
  print("fail")