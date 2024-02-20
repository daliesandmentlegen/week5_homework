import random
#
# computer_input = random.randint(0,2)
# print(computer_input)

# user_input = input("Let's play Rock, Paper Scissors!\nChoose your weapon. R = Rock, P = Paper, S = Scissors: ")

def outcome(computer_input, user_input):
    if user_input == "R" and computer_input == 0:
        print(f"You chose {user_input}, computer chose Rock. It's a draw!")
    elif user_input == "P" and computer_input == 1:
        print(f"You chose {user_input}, computer chose Paper. It's a draw!")
    elif user_input == "S" and computer_input == 2:
        print(f"You chose {user_input}, computer chose Scissors. It's a draw!")
    else:
        player_lose(computer_input, user_input) or player_wins(computer_input, user_input, wins=0)
def player_wins(computer_input, user_input, wins):
    if user_input == "R" and computer_input == 2:
        print(f"You chose {user_input}, computer chose Scissors. You win!")
        wins += 1
    elif user_input == "P" and computer_input == 0:
        print(f"You chose {user_input}, computer chose Rock. You win!")
        wins += 1
    elif user_input == "S" and computer_input == 1:
        print(f"You chose {user_input}, computer chose Paper. You win!")
        wins += 1

def player_lose(computer_input, user_input):
    if user_input == "R" and computer_input == 1:
        print(f"You chose {user_input}, computer chose Paper. You lose!")
    elif user_input == "P" and computer_input == 2:
        print(f"You chose {user_input}, computer chose Scissors. You lose!")
    elif user_input == "S" and computer_input == 0:
        print(f"You chose {user_input}, computer chose Rock. You lose!")

# outcome(computer_input,user_input)