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
    with open("words.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        print(random.choice(words))


def restart_game():
    """
    When the game is finished ask the player if they want to play again. 
    If they don't, tell them thank you for playing
    """
    restart_answer = input("Do you want to play again? Press Y/N \n").lower()
    if restart_answer == "y":
        play_game()
    else:
        print("Thank you for playing! Take care until next time!")


def play_game(word):
    """
    Function to play game
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 8
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")


welcome_to_game()
get_random_word()
restart_game()
play_game()


