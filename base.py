import random
# functions go here

def show_instructions():
    while True:
        question = input("Have you played the game before? ")
        instructions = ("Show Instructions")

        if question == "yes" or question == "y":
            print(instructions)
            return
        elif question == "no" or question == "n":
            print(instructions)
            return
        else:
            print("Please enter yes/no")

def valid_input(question):
    while True:
        response = input((question)).lower()
        valid_inputs = ["rock", "scissors", "paper, gun"
                                        ]

        if response in valid_inputs or response in valid_inputs[0]:
            return response
        elif response == "xxx":
            quit()
        else:
            print("Please choose a valid option eg.(rock, paper or scissors)")


def rounds(question):
    response = input(question)
    while response != "":
        user_choice













show_instructions()
rounds("Press enter for continuous mode: ")
user_choice = valid_input("Please choose rock, paper or scissors: ")



