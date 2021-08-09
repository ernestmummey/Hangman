import random


# Variables
NAME = input('What is your name? ')
WORDS = ["hangman", "hat", "turtle", "tequila", "picture", "vase", "python", "commandline"]
word = random.choice(WORDS)
# Main function for the game
def main():
    print(f"Hello {NAME}!")
    play_game = input("Would you like to play a quick game of Hangman? yes or no \n")

    if  play_game == "yes":
        print("In this Hangman, you will have 7 guesses before you lose the game. Please use only letters of the Alphapet or you will lose that turn. Good Luck!")

        # helper funtion to offically start the game
        startGame()
    else:
        print("Have a good day !")

# helper function to start the guessing of the game
def startGame():
    turn = 7
    guesses = ''

    print("You first guess")

    while turn > 0:
        wrong_guess = 0
        for char in word:
            if char in guesses:
                print(char)
                
            else:
                print("__")
                wrong_guess += 1
        if wrong_guess == 0:
            print("You win")
    
        guess = input("Pick a letter \n")
        guesses += guess

        if guess not in word:
            turn -= 1

        if turn == 0:
            print("You loose")

# This will start the the function call of the main function. Python first looks for a module name "main" then starts the program 
if __name__=="__main__":
    main()