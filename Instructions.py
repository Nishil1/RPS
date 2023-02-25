def show_instructions():
    while True:
        question = input("Have you played the game before? ")
        instructions = "Show Instructions"

        if question == "yes" or question == "y":
            print(instructions)
            return
        elif question == "no" or question == "n":
            print(instructions)
            return
        else:
            print("Please enter yes/no")





