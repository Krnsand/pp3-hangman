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
            print("If you have not guessed the word correctly by the time ")
            print("your lives reaches 0, it is game over.")
            input("When ready to play, press Enter, \n")
            return username
            break


def get_random_word():
    """
    Get random word from words.txt file to play
    """
    random_word = random.choice(open('words.txt', 'r'))
    word = random_word.read()
    random_word.close()
    print(word)


welcome_to_game()
get_random_word()
# start_game()


