import random
# checks users enter a valid choice based on a list
# used for yes / no and r / p / s responses
def choice_checker(question, valid_responses, error):
    while True:
        response = input(question).lower()
        for item in valid_responses:
            if response in valid_responses and (response == "xxx" or response == "x"):
                break

            if response == item[0] or response == item:
                return item
        print(error)


# checks that type of play, regular or # of rounds is valid
def num_check(question):
    error = "Please enter an integer that is more than zero"
    while True:
        response = input(question)
        if response == "":
            return response
        try:
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# main routine goes here

# initialise variables
rounds_played = 1
mode = "regular"

print("*********************************************")
print("**** Welcome to Rock, Paper and Scissors ****")
print("*********************************************")
print()
print()
rps_list = ["rock", "paper", "scissors", "xxx"]
yes_no_list = ["yes", "no", "y", "n"]
# shows instructions if user needs
played_before = choice_checker("Have you played the game before? ",
                               yes_no_list, "Please enter yes/no")
games_won = 0
games_lost = 0
games_drawn = 0
num_of_rounds = 0
if played_before == "no":
    print("You can choose a type of play, either continuous or enter "
          "an amount of rounds. After game ends,"
          "statistics will be displayed")
# asks # of rounds/infinite
rounds_wanted = num_check("How many rounds?  Press <enter> for infinite")

if rounds_wanted == "":
    # sets rounds wanted to practically infinite if user chooses infinite gameplay
    rounds_wanted = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000

# Game loop starts here
while rounds_played < rounds_wanted:
    if mode == "infinite":
        rounds_wanted += 1

    print(f"Round: {rounds_played}")
    user_choice = choice_checker("Enter r, p or s(xxx) to quit: ", rps_list,
                                 "Please enter r, p, s or 'xxx' to quit")
    rounds_played += 1
    # checks for exit code
    if user_choice == "xxx":
        break
        # generates computer choice
    computer_choice = random.choice(rps_list[:-1])
    # decide the winner
    # if it's a draw
    if user_choice == computer_choice:

        print()
        print('{} v {}, =========== draw ============='.format(user_choice, computer_choice))
        games_drawn += 1
        print()
        # checks for possible user wins
    elif (user_choice == "rock" and computer_choice == "scissors") or (
            user_choice == "paper" and computer_choice == "rock") or (
            user_choice == "scissors" and computer_choice == "paper"):
        print()
        print("😀 😀 {} v {}. You won! 😀 😀  ".format(user_choice, computer_choice))
        games_won += 1

        print()
        # displays computer win if draw or user win don't match
    else:
        print()
        print("XXXX {} v {}. You lost! XXXX".format(user_choice, computer_choice))
        games_lost += 1
        print()
# End of game - show stats
print(f"Games won: {games_won}, Games lost: {games_lost}, Games drawn: {games_drawn}")