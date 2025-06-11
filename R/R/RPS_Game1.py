import random

while True:
    # Ask user for their choice
    choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()

    # Valid options
    options = ['s', 'r', 'p']

    # Handle invalid input
    if choice not in options:
        print("Invalid Choice!")
        continue
    
    # Let computer choose randomly  
    pc = random.choice(options)

    # Show both choices
    print("You chose: ", choice)
    print("Computer chose: ",pc)

    # Game outcome logic
    if pc == choice:
        print("It's a Tie!")
    elif((pc == 'r' and choice == 's') or
         (pc == 's' and choice == 'p') or
         (pc == 'p' and choice == 'r')):
        print("You Lose! Try again!")
    else:
        print("You Win! Congrats!")

    # Ask to play again    
    continue_game = input("Play again? (Y/N): ").upper()
    if continue_game == "N":
        print("Thanks for playing!")
        break
