# functions would go here

# main routine goes here

# initialise variables
rounds_played = 0
rounds_wanted = input("How many rounds do you want? ")
mode = "regular"

if rounds_wanted != "":
    rounds_wanted = int(rounds_wanted)

if rounds_wanted == "":
    rounds_wanted = 5
    mode = "infinite"

# ask user if they have played before

# Game loop starts here
while rounds_played < rounds_wanted:

    if mode == "infinite":
        rounds_wanted += 1

    print(f"Round: {rounds_played + 1}")
    user_choice = input("Choose something: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

# End of game - show stats
print("Stats go here")

