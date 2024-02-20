import game_functions

# Set rounds, wins and losses to 0
sets = 0
wins = 0
losses = 0
ties = 0
gamePlay = True

# Starts game
print("Let's play Rock, Paper, Scissors!\n")
rounds = int(input("How many rounds do you want to play: "))  # asks player to enter number of rounds
while sets < rounds:
    # Start the main game loop
    for num in range(rounds):  # repeats rounds according to player input
        # Get player choice
        player = game_functions.play()  # calls upon player choice func in game_func modules

        # Computer randomly chooses rock, paper, scissors
        computer = game_functions.CompChoice()  # randomises then calls upon computer choice func in game_func module

        # Check if there is a tie
        if game_functions.gameTie(player, computer):
            print(f"You chose {player}, the computer chose {computer}!\nIt's a tie!")
            ties += 1

        # Player wins
        elif game_functions.determineWinner(player, computer):
            print(f"You chose {player}, the computer chose {computer}!")
            print(f"\nWinner, winner, chicken dinner! {player} beats {computer}!")
            wins += 1

        # Computer wins
        else:
            print(f"You chose {player}, and the computer chose {computer}!")
            print(f"\nWomp womp, You lost! {computer} beats {player}!")
            losses += 1

        # Round counter
        sets += 1
        print("-------------------------")
        print(f"Round No: {sets}")
        print("------ Score Board ------")
        print(f"Player: {wins} | Computer: {losses} | Ties: {ties}")
        print("===============================")
        print("")
        if sets == rounds:
            gamePlay = False
            break
        #  print(f"Wins: {wins}  Losses:  {losses}   Ties:  {ties}\n")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
