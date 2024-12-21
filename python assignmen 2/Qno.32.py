weather = input("Enter the weather (sunny/rainy): ").strip().lower()

if weather == "sunny":
    print("Great! You can go for outdoor activities like hiking or a picnic.")
elif weather == "rainy":
    rain = input("Do you have a raincoat or umbrella? (yes/no): ")
    if rain == "yes":
        print("You can go to a nearby mall or museum.")
    else:
        print("It's better to stay home and watch movies.")
else:
    print("Sorry, I don't recognize that weather.")
