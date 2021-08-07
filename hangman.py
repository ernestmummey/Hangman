


# Variables
NAME = input('What is your name? ')


# Main function for the game
def main():
    print(f"Hello {NAME}!")
    print("Would you like to play a quick game of Hangman? yes or no")

    if  input() == "yes":
        print("In this Hangman, you will have 7 guesses before you lose the game. Please use only letters of the Alphapet or you will lose that turn. Good Luck!")
        print(" ")
        # helper funtion to offically start the game
        startGame()
    else:
        print("Have a good day !")

# helper function to start the guessing of the game
def startGame():
    counter = 0
    secretWord = "hangman"
    print("Pick a letter ")

    for letter in secretWord:
        if input() == letter:
            print("You guessed right")
            counter += 1
        elif input != letter:
            counter -= 1
            print("Try again")
    if counter == 7:
        print("You win")
        return
    else:
        print("Maybe next time")
            

# This will start the the function call of the main function. Python first looks for a module name "main" then starts the program 
if __name__=="__main__":
    main()