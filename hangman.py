


# Variables
NAME = input('What is your name? ')


# Main function for the game
def main():
    print(f"Hello {NAME}!")
    play_game = input("Would you like to play a quick game of Hangman? yes or no \n")

    if  play_game == "yes":
        print("In this Hangman, you will have 7 guesses before you lose the game. Please use only letters of the Alphapet or you will lose that turn. Good Luck!")
        print(" ")
        # helper funtion to offically start the game
        startGame()
    else:
        print("Have a good day !")

# helper function to start the guessing of the game
def startGame():
    turn = 7
    secretWord = "hangman"
    guess = input("Pick a letter \n")
    char_guess = ' '


    while turn > 0:
        for char in secretWord:
            wrong_guess = 0
            if char in char_guess:
                print(char)
                
            else:
                print("__")
                turn +=1
        if wrong_guess == 7:
            print("You win")
    
        char_guess += guess

        if guess not in secretWord:
            turn -= 1

        if turn == 0:
            print("You loose")

# This will start the the function call of the main function. Python first looks for a module name "main" then starts the program 
if __name__=="__main__":
    main()