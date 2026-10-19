from wordle_functions import *



def main():

    # set initial vatriables
    guess_count = -1

    #intro function
    print()
    print('Welcome to Mystery Wordle!')
    print('Guess the five-letter word.')
    print()
    print('G = correct letter and position\nY = correct letter, wrong position\n- = letter is not in the word\n')

    play_game = True
    past_guesses = []
    #start game loop
    while play_game is True:
        #select word function
        secret_word = select_word()

        guess_count = 0
        #while the # of attempts less than 7
    
        while guess_count < 6:
            #check restart condition
            if guess_count == -1:
                break

            print(f'Attempt {guess_count + 1} of 6')

            # get_guess()       : Gets and validates the player's guess.
            guess = get_guess()
            past_guesses.append(guess)

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
        print(f'Sorry, you have used all your attempts. The secret word was: {secret_word.upper()}')
        again = input('Would you like to play again? (yes/no) ')
        print()
        
        if again == 'no':
            print('Thanks for playing!')
            play_game = False
            return
        
        elif again == 'yes':
            play_game = True
            guess_count = -2
            
        else:
            print('invalid response')
        
            
        


if __name__ == "__main__":
    main()