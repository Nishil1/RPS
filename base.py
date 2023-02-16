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
        response = input(question).lower()
        valid = ["rock", "scissors", "paper"]


        if response in valid or response in valid[0]:
            return response
        elif response == "xxx":
            quit()
        else:
            print("Please choose a valid option eg.(rock, paper or scissors)")









 valid_inputs = ["rock", "scissors", "paper"]


def computer():
    com_choice = random.choice(valid_inputs)
    print(com_choice)





show_instructions()

user_choice = valid_input("Please choose rock, paper or scissors: ")
computer()



