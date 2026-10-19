from functions import *



def main():
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
            print(f'try {guess_count + 1}')

            # get_guess()       : Gets and validates the player's guess.
            guess = get_guess()
            
            # evaluate_guess()  : Compares the guess with the secret word and returns feedback.
            hint = evaluate_guess(guess, secret_word)

            #display_guess()   : Displays the guess and its feedback.
            display_guess(guess, hint)

            #has_won() : Determines whether the player has guessed the word.
            


            guess_count += 1

        play_game = False
            
        


if __name__ == "__main__":
    main()