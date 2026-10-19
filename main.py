from functions import *



def main():

    # set initial vatriables
    guess_count = -1

    #intro function
    print('Welcome to Mystery Wordle!')
    print('Guess the five-letter word.')
    print()
    print('G = correct letter and position\nY = correct letter, wrong position\n- = letter is not in the word\n')

    play_game = True
    #start game loop
    while play_game is True:
        #select word function
        # secret_word = select_word()
        secret_word = 'anuct'
        guess_count = 0
        #while the # of attempts less than 7
    
        while guess_count < 6:
            #check restart condition
            if guess_count == -1:
                break

            print(f'try {guess_count + 1}')

            # get_guess()       : Gets and validates the player's guess.
            guess = get_guess()
            
            # evaluate_guess()  : Compares the guess with the secret word and returns feedback.
            hint = evaluate_guess(guess, secret_word)

            #display_guess()   : Displays the guess and its feedback.
            display_guess(guess, hint)

            #has_won() : Determines whether the player has guessed the word.
            if has_won(hint):
                print('Congratulations! You solved the puzzle.')
                while True:
                    #ask user if they want to play again
                    again = input('Would you like to play again? (yes/no) ')
                    print()
                    
                    if again == 'no':
                        print('Thanks for playing!')
                        play_game = False
                        return
                    
                    elif again == 'yes':
                        play_game = True
                        guess_count = -2
                        break
                    else:
                        print('invalid response')
                        

            guess_count += 1

        
            
        


if __name__ == "__main__":
    main()