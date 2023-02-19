import random
# functions go here

def show_instructions():
    while True:
        question = input("Have you played the game before? ")
        instructions = "Show Instructions"

        if question == "yes" or question == "y":

            return
        elif question == "no" or question == "n":
            print(instructions)
            return
        else:
            print("Please enter yes/no")



def valid_input(question):
    while True:
        response = input(question).lower()
        if response == "r" or response == "rock":
            return response == "r"
        elif response == "s" or response == "scissors":
            return response == "s"
        elif response == "p" or response == "paper":
            return response == "p"
        elif response == "xxx":
            quit()


        else:
            print("Please enter a valid choice eg. rock, paper or scissors")

def type_of_play(question):
    while True:

        response = input(question)
        if response == "":
            print("continuous mode")
            return response

        elif response == "a":
           print()
           return response
        else:
            print("Please enter a valid input to decide type of gameplay")


def who_wins(user, computer):
    if user == computer:
        print("draw")
    elif user == "s" and computer == "p":
        print("You won")
    elif user == "p" and computer == "s":
        print("you lost")
    elif user == "r" and computer == "p":
        print("You lost")
    elif user == "p" and computer == "r":
        print("You won")
    elif user == "r" and computer == "s":
        print("You won")
    elif user == "s" and computer == "r":
        print("You lost")


show_instructions()

# set up addition game rules

#start game

play_type = type_of_play("Press <enter> to enter continuous "
                "mode or press 'a' to set the amount of rounds")


user_choice = valid_input("Please choose rock, paper or scissors or type 'xxx' to quit: ")





