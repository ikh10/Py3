import random

# Valid options
emojis = {'r': '🪨', 'p': '📄', 's': '✂️'} # Use dictionary
options = ['r', 'p', 's'] # Use list

while True:
    # Ask user for their choice
    user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()

    # Validate input
    if user_choice not in options:
        print("Invalid Choice!")
        continue
    
    # Let computer choose randomly  
    computer_choice = random.choice(options)

    # Show both choices
    print("You chose: ", emojis[user_choice])
    print("Computer chose: ", emojis[computer_choice])

    # Game outcome logic
    if computer_choice == user_choice:
        print("It's a Tie!")
    elif((computer_choice == 'r' and user_choice == 's') or
         (computer_choice == 's' and user_choice == 'p') or
         (computer_choice == 'p' and user_choice == 'r')):
        print("You Lose! Try again!")
    else:
        print("You Win! Congrats!")

    # Ask to play again    
    continue_game = input("Play again? (Y/N): ").upper()
    if continue_game == "N":
        print("Thanks for playing!")
        break
