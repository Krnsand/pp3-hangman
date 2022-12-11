import random
import string
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')

scoreboard = SHEET.worksheet("scores")
#data = scores.get_all_values()
score = 0


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
# start_game()
game_rules()


