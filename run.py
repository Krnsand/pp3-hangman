import gspread
from google.oauth2.service_account import Credentials
import random
import string

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


"""
Assign credentials from my API's and access scores spreadsheet
"""
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')

scoreboard = SHEET.worksheet("scores")
#data = scores.get_all_values()
score = 0


class TextColors:
    """
    Define the different text colors to be used
    """
    BLUE = '\033[38;5;159m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'


def welcome_to_game():
    """
    Welcome user to game and ask for their name. Show logo
    """
    print("{}    {}    {}{}     {}    {}    {}}}}}    {}      {}    {}{}     {}    {}")
    print("{}    {}   {}  {}    {}}}  {}   {}    {}   {}}}  {{{}   {}  {}    {}}}  {}")
    print("{}{{}}{}  {}{{}}{}   {} {} {}   {}         {} {{}} {}  {}{{}}{}   {} {} {}")
    print("{}    {}  {}    {}   {}  {{{}   {}  {{{{   {}  {}  {}  {}    {}   {}  {{{}")
    print("{}    {}  {}    {}   {}    {}    {}}}}}    {}      {}  {}    {}   {}    {} \n")

    username = " "
    while True:
        username = input("Welcome! Please enter your name: \n")

        if username.isalnum() is not True:
            print("Error: Letters and numbers only. \n")

        else:
            print(f"Hi {username}, You have up to 8 guesses to guess the Word.")
            input("When ready to play, press Enter. \n")
            return username
            break


def get_random_word():
    """
    Gets a random word from word.txt for each round
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    return random_word.upper()


def start_game():
    """
    Start the game or view the rules of the game
    """
    lives = 8
    guesses = []
    complete = False
    word_template = "_" * len(word)
    print(f" Lives: {lives}\n")
    print(f" The word to guess: " + " ".join(word_template) + "\n")

    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # getting user input
    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in used_letters:
            word_letters.remove(used_letters)
    
    elif user_letter in used_letters:
        print("You have already guessed that letter. Please guess again.")

    else:
        print("Invalid character. Please choose a letter.")


welcome_to_game()
get_random_word()
start_game()
#game_rules()


def game_rules():
    """
    Define the rules of the game
    """
    print(
        """
        Guess a letter for the random word.
        Is your letter in the word? Great! You continue without
        losing a life. Is it not? Sorry! You lose a life. When your 
        lives reach 0 without having guessed the word correctly, it
        is game over.
        """
            )
