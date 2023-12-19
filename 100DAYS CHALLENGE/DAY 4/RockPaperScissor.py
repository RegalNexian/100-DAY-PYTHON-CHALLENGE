import random

print("Let's play Rock, Paper, Scissors!")
user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)

print(f"Your choice: {user_choice}")
print(f"Computer's choice: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "Rock" and computer_choice == "Scissors") or \
     (user_choice == "Paper" and computer_choice == "Rock") or \
     (user_choice == "Scissors" and computer_choice == "Paper"):
    print("You win!")
else:
    print("Computer wins!")
