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


def initialise_game():
    """
    Option to begin game or select difficulty
    """
    print(" Press " + TextColors.BLUE + "1" + TextColors.WHITE +
           " to play game")
    print(" Press " + TextColors.BLUE + "2" + TextColors.WHITE +
           " to set difficulty")
    print(" Press " + TextColors.BLUE + "3" + TextColors.WHITE +
          " to view rules")
    options = False
    while not options:
        settings = input("\n ")
        if settings == "1":
            options = True
            difficulty = "default"
            return difficulty

        elif settings == "2":
            options = True

        elif settings == "3":
            options = True
            game_rules()

        else:
            print(TextColors.RED + " Please select 1, 2 or 3 to make your"
                  " choice" + TextColors.WHITE)


