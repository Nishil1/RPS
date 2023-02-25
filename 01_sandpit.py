def string_check(question, valid_responses, error):
    print(question)
    print(valid_responses)
    print(error)


check_yes_no = string_check("Is this ok", ["yes", "no"], "You need to say yes / no")
check_rps = string_check("choose rps", ["rock", "paper", "scissors"], "choose rps")