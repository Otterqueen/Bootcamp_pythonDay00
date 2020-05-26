import sys
import random


print("\nThis is an interactive guessing game!\n \
You have to enter a number between 1 and 99 to find out the secret number.\n\
Type 'exit' to end the game.\n\
Good luck!\n")
cmpt = 0
goal = random.randint(1, 99)

while 1:
    cmpt = cmpt + 1
    input_user = input("What's your guess between 1 and 99?\n")
    if input_user == "exit":
        print("Goodbye!")
        sys.exit()
    else:
        try:
            input_user = int(input_user)
            if input_user == 42:
                print("The answer to the ultimate question of life, \
the universe and everything is 42.\n")
            if input_user < goal:
                print("Too low!\n")
            elif input_user > goal:
                print("Too high!\n")
            else:
                print("You won in " + str(cmpt) + " attempts!")
                sys.exit()
        except ValueError:
            print("That's not a number.\n")
