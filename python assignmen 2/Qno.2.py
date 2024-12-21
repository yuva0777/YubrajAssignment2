print("Welcome to Treasure Land!")
print("Your mission is to find the treasure.")
direction = input("Do you want to go 'left' or 'right'? ").lower()

if direction == "right":
    print("Game Over. You fell into a trap!")
else:
    action = input("You've reached a lake. Do you want to 'swim' or 'wait'? ").lower()
    
    if action == "swim":
        print("Game Over. You were attacked by crocodiles!")
    else:
        # Step 3: Choose a door color
        color = input("You see three doors: one 'red', one 'blue', and one 'yellow'. Which one do you choose? ").lower()
        
        if color == "red":
            print("Game Over. You were burned by fire!")
        elif color == "blue":
            print("Game Over. You were eaten by beasts!")
        elif color == "yellow":
            print("Congratulations! You found the treasure! You Win!")
        else:
            print("Game Over. You chose a door that doesn't exist.")

