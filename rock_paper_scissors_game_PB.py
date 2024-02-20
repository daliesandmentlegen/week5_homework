import random, game_functionsdirectory

max_attempts = 3
attempts = 1
wins = 0

while True:
    user_input = input("Let's play Rock, Paper Scissors!\nChoose your weapon. R = Rock, P = Paper, S = Scissors: ")
    computer_input = random.randint(0, 2)
    print(computer_input)

    game_functionsdirectory.outcome(computer_input, user_input)

    attempts += 1
    print(f"Round #{attempts}\nNumber of win {wins}")

    play_again = input("Play again? (y/n): ")
    print(50 * "#")
    if play_again.lower() != "y":
        print(f"Game Over! You scored {wins} out of {attempts} games")
        print(50 * "#")
        break


    # if play_again.lower() != "y":
    #     print(50 * "#")
    #     break









#
# computer_input = random.choice(range(0,3,k=3))
# print(computer_input)
# #
# # while loop. user_input/pass will be requested whilst the while statement is true (attempts is less than max attempts
# while attempts < max_attempts:
#     user_weapon = input("Choose your weapon. 0 = Rock, 1 = Paper, 2 = Scissors: ")
#     user_input = user_weapon.upper()
#     print(user_input)
#     print(computer_says)
# # check if the entered username and password are correct
# # conditions to define response to correct and incorrect information inputted
#     if user_action == computer_action:
#         print(f"Both players selected {user_action.name}. It's a tie!")
#     elif user_action == Action.Rock:
#         if computer_action == Action.Scissors:
#             print("Rock smashes scissors! You win!")
#         else:
#             print("Paper covers rock! You lose.")
#     elif user_action == Action.Paper:
#         if computer_action == Action.Rock:
#             print("Paper covers rock! You win!")
#         else:
#             print("Scissors cuts paper! You lose.")
#     elif user_action == Action.Scissors:
#         if computer_action == Action.Paper:
#             print("Scissors cuts paper! You win!")
#         else:
#             print("Rock smashes scissors! You lose.")

#
#
#
#
#
#
# #     if user_input == computer_says:
# #         print("It's a draw! Try Again")
# #         score = 0
# # # if user_input and pass combination is correct, break the while loop
# #     else:
# #         attempts += 1
# #         remaining_rounds = max_attempts - attempts
# #         print(f"{remaining_rounds} rounds left")
# # # if number max attempts have been reached, print 'blocked' message
# #
# # if attempts == max_attempts:
# #     print("The winner is____")
#
#
#
#
#
#


#
# class Action(IntEnum):
#     Rock = 0
#     Paper = 1
#     Scissors = 2
# def player_selection():
#     player_input = input('Enter Rock ("R"), Paper ("P") or Scissors ("S")')
#     selection = int(player_input)
#     action = Action(selection)
#     return action
#
# player_selection(Rock)