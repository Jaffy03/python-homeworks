import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

def play_game():
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("First to 5 points wins the match.\n")

    while player_score < 5 and computer_score < 5:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.\n")
            continue

        computer_choice = get_computer_choice()
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        if result == "player":
            player_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

        print(f"Score: Player {player_score} - Computer {computer_score}\n")

    if player_score == 5:
        print("Congratulations! You won the match!")
    else:
        print("Sorry, the computer won the match.")

# Start the game
play_game()