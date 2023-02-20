import random
# functions go here

# this function shows instructions when nesssacary
def show_instructions():
    while True:
        question = input("Have you played the game before? ")
        if question == "yes" or question == "y":
            return
        elif question == "no" or question == "n":
            print('show instruction')
            return
        else:
            print("Please enter yes/no")

# Function make sures that the user input to the mode of gameplay is valid
def capture_number_of_rounds(question):
    while True:
        type_of_play = input(question)
        error = "Please click enter to enter infinity mode or set an amount of rounds"
        if type_of_play != "":
            try:
                type_of_play = int(type_of_play)
                if type_of_play < 1:
                    print(error)
                    continue
            except ValueError:
                print(error)
                continue
        return type_of_play

# makes sures user input is valid eg.(rock, paper, scissors or "xxx" to quit)
def capture_and_validate_user_input(question):
    while True:
        response = input(question).lower()
        scissor = ["scissors", "scissor", "s"]
        rock = ["r", "rock", "rocks"]
        paper = ["p", "paper", "papers"]
        if response in scissor:
            return "scissors"
        elif response in rock:
            return "rock"
        elif response in paper:
            return "paper"
        elif response == "xxx":
            quit("Exiting the game,Thanks for playing!")
        else:
            print("Please enter rock, paper or scissors")


def calculate_computer_input():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    print('Computer choice: ', computer_choice)
    return computer_choice;

# takes the user input and prints/outputs the winner whilst generating a random value for the computer choice
def decide_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        user_details['games_drawn'] += 1;

        print('draw');
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        user_details['games_won'] += 1;

        print('user winner');
    else:

        user_details['games_lost'] += 1;
        print('computer win')

    user_details['number_of_rounds'] +=1;


def display_results(user):
    print("Games won: {}, Games lost: {}, Games drawn: {}".format(user['games_won'], user["games_lost"], user["games_drawn"]));


# This function contains gameplay components eg.(rounds, messages alerting
# the user whether they won or lost etc) different to each mode
def start_game():
    rounds = 1
    if amount_of_chosen_rounds != "": #user selected specific number of rounds
        while rounds <= amount_of_chosen_rounds:
            print("Round: {} of {}".format(rounds, amount_of_chosen_rounds))
            user_choice = capture_and_validate_user_input("Choose rock, paper or scissors or enter 'xxx' to quit: ")
            computer_choice = calculate_computer_input();
            decide_winner(user_choice,computer_choice)
            rounds += 1
        display_results(user_details);


    else:
        while True:
            print("Continuous Mode: Round {}".format(rounds))
            user_choice = capture_and_validate_user_input("Choose rock, paper or scissors or enter 'xxx' to quit: ")
            computer_choice = calculate_computer_input();
            decide_winner(user_choice, computer_choice)
            rounds += 1
            display_results(user_details);

# main routine starts here
print("*********************************************")
print("**** Welcome to Rock, Paper and Scissors ****")
print("*********************************************")
print()
print()
user_details = {
      "name": "End User",
      "games_won": 0,
      "games_lost": 0,
      "games_drawn": 0,
      "number_of_rounds": 0
}


amount_of_chosen_rounds = capture_number_of_rounds\
    ("Please press <enter> to enter infinite mode or enter # of rounds:  ")
start_game();