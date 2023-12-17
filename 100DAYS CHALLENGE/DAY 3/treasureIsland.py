print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.\n")

print("You are on a deserted island. To your left, there is a jungle, and to your right, there is a cave.")
direction_choice = input("Which direction do you choose? (left/right): ").lower()

if direction_choice == "left":
    print("You venture into the jungle and encounter a pack of wild animals. Game Over! 🦁🌿")
elif direction_choice == "right":
    print("You enter the cave and find three doors: red, blue, and yellow.")
    
    door_choice = input("Which door do you choose? (red/blue/yellow): ").lower()
    
    if door_choice == "red":
        print("You entered the red door and are engulfed in flames. Game Over! 🔥")
    elif door_choice == "blue":
        print("You entered the blue door and are attacked by a fierce beast. Game Over! 🐉")
    elif door_choice == "yellow":
        print("Congratulations! You entered the yellow door and found the treasure! You win! 🎉🏆")
    else:
        print("You didn't choose a valid door. Game Over! 🚪")
else:
    print("You didn't choose a valid direction. Game Over! 🚷")

print("\nThanks for playing Treasure Island!")
