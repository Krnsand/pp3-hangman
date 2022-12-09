import gspread
from google.oauth2.service_account import Credentials
import random

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
        username = input("Welcome! Please enter your Name: \n")

        if username.isalnum() is not True:
            print("Error: Letters and numbers only.")

        else:
            print(f"Hi {username}, You have up to 8 guesses to guess the Word.")
            input("When you are ready to play, press 1 to start \n")
            return username
            break


def start_game():
    """
    Start the game or view the rules of the game
    """

    if 

    print("Press" + TextColors.GREEN + "1" + TextColors.WHITE +
         "to start game")
    print("Press" + TextColors.GREEN + "2" + TextColors.WHITE +
         "to view game rules")


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

welcome_to_game()
game_rules()

