import random

def game_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors! (type 'exit' to quit)\n")

    while True:
        player_choice = input("Enter rock, paper, or scissors: ").strip().lower()

        if player_choice == "exit":
            print("Thanks for playing!")
            break

        if player_choice not in choices:
            print("Invalid choice! Please try again.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        result = game_result(player_choice, computer_choice)
        print(result)
        print("-" * 40)

play_game()