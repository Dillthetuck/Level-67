from random import randint

def select_word():
    word_bank = [
    "lemon", "kudos", "xylan", "cloud", "quota", "night", "agile", "shame", "drink", "ulcer",
    "spicy", "crane", "often", "olive", "sound", "lousy", "music", "yacht", "tiger", "juice",
    "hotel", "flour", "ideal", "zebra", "unity", "maple", "venom", "globe", "weird", "image",
    "charm", "month", "plume", "quiet", "table", "lurch", "zilch", "nurse", "vocal", "delta",
    "jaunt", "fable", "knead", "knife", "elbow", "radio", "punch", "pride", "built", "inbox",
    "zoned", "magic", "apron", "noble", "earth", "joint", "piano", "rocky", "frisk", "quick",
    "ghost", "bonus", "beard", "realm", "valid", "empty", "uncle", "light", "xeric", "faith",
    "about", "young", "orbit", "yearn", "nymph", "wrist", "giant", "skirt", "virus", "tulip",
    "quilt", "hound", "grape", "woman", "zesty", "brick", "ocean", "thorn", "cyber", "risky",
    "waltz", "diary", "eight", "heart", "human", "ivory", "yield", "aside", "donut", "upset",
]
    return word_bank[randint(0,99)]


# get_guess()       : Gets and validates the player's guess.
def get_guess():
    while True:
        guess = input('Enter a five-letter word: ').strip()
        
        if len(guess) != 5:
            print("Invalid input: The word must be exactly 5 letters long.")
        elif not guess.isalpha():
            print("Invalid input: Please enter letters only")
        else:
            return guess



# evaluate_guess()  : Compares the guess with the secret word and returns feedback.
def evaluate_guess(guess, secret):
    hint = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            hint.append('G')
        elif guess[i] == secret[0] or guess[i] == secret[1] or guess[i] == secret[2] or guess[i] == secret[3] or guess[i] == secret[4]:
            hint.append('Y')
        else:
            hint.append('-')
    return hint

#display_guess()   : Displays the guess and its feedback.
def display_guess(guess, hint):
    print(f'Guess: {guess[0].upper()} {guess[1].upper()} {guess[2].upper()} {guess[3].upper()} {guess[4].upper()}')
    print(f'Feedback: {hint[0]} {hint[1]} {hint[2]} {hint[3]} {hint[4]}')
    