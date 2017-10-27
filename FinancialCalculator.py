#!/usr/bin/env python

"""FinancialCalculator.py: Stores entries of bills or other financially related
entries that helps the user keep track of his/her monthly finances and thus be  
more financially responsible."""

__author__      = "Peter Chea"
__version__     = "1.0"
__email__       = "longkchea@gmail.com"
__status__      = "production"

# Messages
start_msg = "Welcome to the Financial Tracker, where we can help you with \
managing your finances\n"
choice_msg1 = "Please enter one of the following choices:\n\
    1. Add an entry\n    2. Delete an entry\n    q. Quit\n"
choice_msg1_error = "I'm sorry, your input did not make sense to me.\
\nPlease try again.\n"
entry_msg = "Type each new entry in the format entry, value. \
\nExample: Laundry, 500:\n(When you are done, type:\ndone,\n"
quit_msg = "Closing program...\n" 

# Greet the user
print(start_msg)

# Main loop
while True: 
    isValid = False
    choice = ""

    # This loop will only break if the choice made by the user is valid
    while (not isValid):
        # Ask user for choice
        choice = input(choice_msg1)
        if (choice == "1" or choice == "2" or choice.lower() == "q"):
            isValid = True
            break
        else: 
            print (choice_msg1_error)

    finances = {}
    if choice == "1": 
        user_input = []
        print(entry_msg)
        # Takes input from the user in the form of a list of tuples
        while True: 
            user_input.append(tuple(input().replace(" ","").split(",")))
            if user_input[-1] == ('done', ''):
                del user_input[-1]
                break

        # Copy all valid entries over to a new list using lambda func
        new_user_list = list(filter(lambda x: x[1:] is not (), user_input))
                
        for (i,j) in new_user_list: 
            finances[i] = j
        
        print("Here is your list: {}".format(finances.items()))

    if choice.lower() == "q": 
        print(quit_msg)
        break


