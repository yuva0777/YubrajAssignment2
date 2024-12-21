print("Welcome to the Haunted House!")
choice1 = input("Do you want to go upstairs or downstairs? ")

if choice1 == "downstairs":
    print("Game Over.")
elif choice1 == "upstairs":
    choice2 = input("Do you want to enter the room or stay outside? ")

    if choice2 == "enter the room":
        print("Game Over.")
    elif choice2 == "stay outside":
        choice3 = input("Do you want to choose ghost, vampire, or werewolf? ")

        if choice3 == "ghost" or choice3 == "vampire":
            print("Game Over.")
        elif choice3 == "werewolf":
            print("You Win!")
        else:
            print("Invalid choice. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("Invalid choice. Game Over.")
