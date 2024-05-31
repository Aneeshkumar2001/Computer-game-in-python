import random

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']
    

    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while player_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    
    
    computer_choice = random.choice(choices)
    
   
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win! Computer chose", computer_choice)
    else:
        print("You lose! Computer chose", computer_choice)


if __name__ == "__main__":
    play_game()
1