import random

def determine_winner(player_choice, cpu_choice):
    if player_choice == cpu_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and cpu_choice == 'scissors') or \
         (player_choice == 'scissors' and cpu_choice == 'paper') or \
         (player_choice == 'paper' and cpu_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors Game!")
    player_score = 0
    cpu_score = 0

    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        player_choice = input("Enter your choice (1/2/3/4): ")

        if player_choice == "4":
            print("Thanks for playing!")
            break
        elif player_choice not in ["1", "2", "3"]:
            print("Invalid choice! Please enter a number between 1 and 4.")
            continue

        player_choice = int(player_choice)
        if player_choice == 1:
            player_move = "rock"
        elif player_choice == 2:
            player_move = "paper"
        else:
            player_move = "scissors"

        cpu_move = random.choice(["rock", "paper", "scissors"])

        print("Your move:", player_move)
        print("Computer's move:", cpu_move)

        result = determine_winner(player_move, cpu_move)
        print("Result:", result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            cpu_score += 1

        print("Your score:", player_score)
        print("Computer's score:", cpu_score)

if __name__ == "__main__":
    main()
