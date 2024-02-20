import random


# Prompts player until they enter "rock", "paper", or "scissors"
def play():
    user = input("Please select rock, paper or scissors: ")
    while user != "rock" and user != "paper" and user != "scissors":
        print("No dice! Try typing rock, paper or scissors")
        user = input("Please select rock, paper or scissors: ")
    return user
    # while True:
    #     print("Please type [R] for Rock, [P] for paper or [S] for scissors: ")
    #     user = input().upper()
    #     if user == 'R':
    #         print('You chose ROCK')
    #     elif user == 'P':
    #         print('You chose PAPER')
    #     elif user == 'S':
    #         print('You chose SCISSORS')
    #     elif user != "R" and user != "P" and user != "S":
    #         print("No dice! Try [R] for Rock, [P] for paper or [S] for scissors")
    #     else:
    #         continue
    #     break
    # return user


# Randomly selects either "rock", "paper" or "scissors" to return
def CompChoice():
    computer = random.randint(0, 2)
    if computer == 0:
        return "rock"
    elif computer == 1:
        return "paper"
    else:
        return "scissors"


# Returns true if there is a tie, false otherwise
def gameTie(user, comp):
    return user == comp


# Returns true if the player wins, false otherwise
def determineWinner(user, comp):
    user_wins = (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (
            user == "scissors" and comp == "paper")
    return user_wins


if __name__ == '__main__':
    play()
