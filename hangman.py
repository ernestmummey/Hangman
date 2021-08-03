

################################################################################################
#                                             Variables
################################################################################################

NAME = input('What is your name? ')

def main():
    print(f"Hello {NAME}!")
    print("Would you like to play a quick game of Hangman? yes or no")

    if  input() == "yes":
        print("In this Hangman, you will have 7 guesses before you lose the game. Please use only letters of the Alphapet or you will lose that turn. Good Luck!")
        print(" ")
        startGame()
    else:
        print("Have a good day !")


def startGame():
    input("Pick a letter ")


if __name__=="__main__":
    main()