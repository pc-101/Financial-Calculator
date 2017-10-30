#!/usr/bin/env python

"""FinancialCalculator.py: Stores entries of bills or other financially related
entries that helps the user keep track of his/her monthly finances and thus be  
more financially responsible."""

__author__      = "Peter Chea"
__version__     = "1.0"
__email__       = "longkchea@gmail.com"
__status__      = "Almost Complete"

import json
from pathlib import Path

# Messages:
# Choice 1: Main choice; User chooses to add or delete an entry or quit
# Choice 2: After inputting entries, user decides to see the list
# Choice 3: Following choice 2, user can decide to finalize the list
# Choice 4: View current monthly totals
start_msg = "Welcome to the Financial Tracker, where we can help you with \
managing your finances." 
choice_msg1 = "Please enter one of the following choices:\n\
    1. Add an entry\n    2. Delete an entry\n\
    3. View current list\n    4. View current monthly totals\n\
    q. Quit\n"
choice_msg_error1 = "I'm sorry, your input did not make sense to me.\
\nPlease try again.\n"
choice_msg_error4 = "I'm sorry, the entry does not exist in your list.\
\nPlease try again.\n"
entry_msg = "Type each new entry in the format entry, value. \
\nWe recommend that underscores(_) or hypens(-) are used to separate\
\nmultiple-worded entries\
\n(Example: Laundry, 500)\
\nWhen you are done, type:\ndone, \n\n"
quit_msg = "Closing program...\n" 
choice_msg2 = "Would you like to see the list? (y/n)\n"
choice_msg3 = "Finalize this list?\n"
choice_msg4 = "Which entry would you like to delete or modify? \
\n(Or press q to go back)\n"
choice_msg5 = "What value would you like this to be? \
\n(A value of 0 deletes this entry from the list)\n"

# Global dictionary to keep track of user's finances 
finances = {}
total = 0.00

# If the finances.txt file exists, we set finances to the previously
# written data
isFile = False
my_file = Path("finances.txt")
if my_file.is_file():
    with open("finances.txt", "r") as f: 
        isFile = True
        my_data = json.load(f)
        finances = my_data
else: 
    total = 0

# Greet the user
print(start_msg)

# Main loop
while True: 
    isValid = False
    choice = ""

    # This loop will only break if the choice made by the user is valid
    while (not isValid):
        # Ask user for choice
        choice = input(choice_msg1).replace(" ","")
        if (choice == "1" or choice == "2" or choice == "3" \
            or choice == "4" or choice.lower() == "q"):
            isValid = True
            break
        else: 
            print (choice_msg_error1)

    # Handle case #1: User adds entry/entries to dictionary
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
        # Copy again, converting list of tuples into a dictionary for easy access
        for (i,j) in new_user_list: 
            finances[i] = j
        
        # Ask if user wants to see the list
        choice2 = input(choice_msg2).replace(" ","").lower()
        while True: 
            if choice2 == 'y': 
                print("Here is your list: {}\n".format(finances.items()))
                break
            if choice2 == 'n':
                break
            if choice2 is not 'y' or choice2 is not 'n': 
                choice2 = input(choice_msg_error1).replace(" ","").lower()
  
        # Ask if user wants to finalize this "list". Choosing 'n' loops
        # back to the beginning of the program, prompting to add/delete
        # items in the dictionary
        choice3 = input(choice_msg3).replace(" ","").lower()
        while True: 
            if choice3 == 'y':
                with open("finances.txt", "w") as file: 
                    file.write(json.dumps(finances))
                print("List has been finalized\n")
                break
            if choice3 == 'n':
                break
            if choice3 is not 'y' or choice3 is not 'n': 
                choice2 = input(choice_msg_error1).replace(" ","").lower()

    # Handle case #2: User deletes entry/entries from dictionary
    if choice == "2":
        while True: 
            print("Here is your list: {}\n".format(finances.items()))
            choice4 = input(choice_msg4).replace(" ","").lower()

            # We allow the user to type in the value to alter
            if choice4 in finances: 
                change_input = input(choice_msg5)
                if change_input == "0": 
                    del finances[choice4]
                else: 
                    finances[choice4] = change_input
                with open("finances.txt", "w") as file: 
                    file.write(json.dumps(finances))
                print("Change has been made\n")
                break
            elif choice4 == "q":
                break
            else:
                print(choice_msg_error4)
    
    # Handle case #3: Viewing the current list
    if choice == "3": 
        print("Here is your list: {}\n".format(finances.items()))

    # Handle case #4: Viewing the current monthly total
    if choice == "4": 
        if isFile: 
            for key in finances: 
                total += float(finances[key])
        print("Your totals for this month: ${:.2f}\n".format(total))

    if choice.lower() == "q": 
        print(quit_msg)
        break


