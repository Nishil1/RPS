import random


# functions go here


# this function contains game statistics and displays them when needed
def display_game_statistics():
    print("---------- Game History -----------")
    display_results(user_statistics)
    print("Thanks for playing")
    quit()

# this function validates user input for instructions question and rock, paper and scissors


def choice_checker(question, valid_responses, error):
    while True:
        response = input(question).lower()
        for item in valid_responses:
            if response == item[0] or response == item:
                return item

            # displays game statistics if user quits by using xxx exit code
            elif response in valid_responses and response == "xxx":
                display_game_statistics()

        print(error)

# Function make sures that the user input to the mode of gameplay is valid


def capture_number_of_rounds(question):
    while True:
        type_of_play = input(question)
        error = "Please click enter to enter infinity mode or set an amount of rounds"
        if type_of_play != "":
            try:
                # converts to int if user doesn't choose infinite mode
                type_of_play = int(type_of_play)
            # checks if # of rounds entered is less than 1
                if type_of_play < 1:
                    print(error)
                    continue
                    # checks if input is not an int
            except ValueError:
                # displays error
                print(error)
                continue
        return type_of_play


# makes sures user input is valid eg.(rock, paper, scissors or "xxx" to quit)
def calculate_computer_input():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    print('Computer choice:', computer_choice)
    return computer_choice


# takes the user input and prints/outputs the winner whilst generating a random value for the computer choice
def decide_winner(user_choice, computer_choice):
    # if it is a draw
    if user_choice == computer_choice:
        user_statistics['games_drawn'] += 1
        print()
        print('{} v {}, =========== draw ============='.format(user_choice, computer_choice))
        print()
        # checks for possible user wins
    elif (user_choice == "rock" and computer_choice == "scissors") or (
            user_choice == "paper" and computer_choice == "rock") or (
            user_choice == "scissors" and computer_choice == "paper"):
        user_statistics['games_won'] += 1
        print()
        print("😀 😀 {} v {}. You won! 😀 😀  ".format(user_choice, computer_choice))
        print()
        # displays computer win if draw or user win don't match
    else:
        user_statistics['games_lost'] += 1
        print()
        print("XXXX {} v {}. You lost! XXXX".format(user_choice, computer_choice))
        print()
    user_statistics['number_of_rounds'] += 1

# function to display results using


def display_results(user):
    print("Games won: {}, Games lost: {}, Games drawn: {}".format(user['games_won'], user["games_lost"],
                                                                  user["games_drawn"]))

# This function contains gameplay components e.g.(rounds, messages alerting
# the user whether they won or lost)


def start_game():
    rounds = 1
    if amount_of_chosen_rounds != "":  # user selected specific number of rounds
        while rounds <= amount_of_chosen_rounds:

            print("Round: {} of {}".format(rounds, amount_of_chosen_rounds))
            print()
            user_choice = choice_checker("Choose rock, paper or scissors", rps_list,
                                         "please enter rock, paper or scissors")

            computer_choice = calculate_computer_input()
            decide_winner(user_choice, computer_choice)
            rounds += 1
        display_game_statistics()

    else:
        while True:
            print("Continuous Mode: Round {}".format(rounds))
            print()

            user_choice = choice_checker("Choose rock, paper or scissors", rps_list,
                                         "please enter rock, paper or scissors")
            computer_choice = calculate_computer_input()
            decide_winner(user_choice, computer_choice)
            rounds += 1

# main routine starts here


print("*********************************************")
print("**** Welcome to Rock, Paper and Scissors ****")
print("*********************************************")
print()
print()
rps_list = ["rock", "paper", "scissors", "xxx"]
yes_no_list = ["yes", "no", "y", "n"]
# shows instructions if user needs
played_before = choice_checker("Have you played the game before?", yes_no_list, "Please enter yes/no")

if played_before == "no":
    print("You can choose a type of play, either continuous or enter an amount of rounds. After game ends,"
          "statistics will be displayed")

# details of user
user_statistics = {
    "games_won": 0,
    "games_lost": 0,
    "games_drawn": 0,
    "number_of_rounds": 0
}

# gets number of rounds
amount_of_chosen_rounds = capture_number_of_rounds("Please press <enter> to enter infinite mode or enter # of rounds: ")

# starts the game after capturing the appropriate game type
start_game()
