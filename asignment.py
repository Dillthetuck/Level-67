
"""
Course: IS 303 – Hilton
Level #: 7
Assignment: Wordle

Description:
Create a Python word-guessing game inspired by Wordle. The computer selects a 
secret five-letter word, and the player gets six attempts to guess it with 
feedback provided after each attempt.

Feedback Guide:
- G (Green): Correct letter and correct position.
- Y (Yellow): Correct letter, but wrong position.
- - (Dash): Letter does not appear in the word.

Program Requirements:
1. Create at least two files: main.py and wordle_functions.py.
2. Welcome the player.
3. Select a secret five-letter word.
4. Give the player up to six guesses.
5. Require each guess to contain exactly five letters.
6. Reject guesses that have already been used.
7. Display feedback after every guess.
8. Tell the player when a letter is correct, misplaced, or absent.
9. End the game when the player guesses the word or uses all six attempts.
10. Display the secret word if the player loses.
11. Ask whether the player would like to play again.

Required Functions (to be implemented in wordle_functions.py):
- choose_word()     : Selects and returns a secret word.
- get_guess()       : Gets and validates the player's guess.
- evaluate_guess()  : Compares the guess with the secret word and returns feedback.
- display_guess()   : Displays the guess and its feedback.
- has_won()         : Determines whether the player has guessed the word.

Additional Guidelines:
- Import functions from wordle_functions.py into main.py.
- Use a list to store previous guesses.
- Use meaningful variable and function names.
- Include comments explaining important sections.
- Do not use classes or advanced Python features not yet covered.
- Note: Secret words do not need to contain repeated letters for the basic version.
"""

# ==========================================
# SAMPLE SESSION
# ==========================================
# Welcome to Mystery Wordle!
# Guess the five-letter word.
# 
# G = correct letter and position
# Y = correct letter, wrong position
# - = letter is not in the word
# 
# Attempt 1 of 6
# Enter a five-letter word: crane
# Guess: C R A N E
# Feedback: - - G G -
# 
# Attempt 2 of 6
# Enter a five-letter word: slate
# Guess: S L A T E
# Feedback: - G G - -
# 
# Attempt 3 of 6
# Enter a five-letter word: plant
# Guess: P L A N T
# Feedback: G G G G G
# 
# Congratulations! You solved the puzzle.
# Would you like to play again? no
# Thanks for playing!
# ==========================================








# create a word_bank list with a butt ton of words in it (no words with repeat numbers)

# choose a word function
# choose_word()     : Selects and returns a secret word.(create in a seperate file)

# Create a function that takes the players guess
# get_guess()       : Gets and validates the player's guess.

# Create an evaluation function (If solution(string) [0] == guess(string) [0]...)
# evaluate_guess()  : Compares the guess with the secret word and returns feedback.

#Create display function using the grading logic
#display_guess()   : Displays the guess and its feedback.

# create a winning function that checks if the player has won
#has_won()         : Determines whether the player has guessed the word.

