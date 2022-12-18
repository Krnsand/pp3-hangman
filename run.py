"""
Import the random choice function and gspread to access score spreadsheet, as
well as import the credentials
"""
import random
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
score = scoreboard.get_all_values()


class TextColors:
    """
    Define the different text colors to be used
    """
    BLUE = '\033[38;5;159m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    YELLOW = '\033[33m'
    BOLD = '\033[1m'


def welcome_to_game():
    """
    Welcome user to game and ask for their name. Show logo
    """
    print(TextColors.RED + "{}    {}    {}{}     {}    {}    {}}}}}    {}    "
          "  {}    {}{}     {}    {}")
    print("{}    {}   {}  {}    {}}}  {}   {}    {}   {}}}  {{{}   {}  {}    "
          "{}}}  {}")
    print("{}{{}}{}  {}{{}}{}   {} {} {}   {}         {} {{}} {}  {}{{}}{}   "
          "{} {} {}")
    print("{}    {}  {}    {}   {}  {{{}   {}  {{{{   {}  {}  {}  {}    {}   "
          "{}  {{{}")
    print("{}    {}  {}    {}   {}    {}    {}}}}}    {}      {}  {}    {}   "
          "{}    {} \n" + TextColors.WHITE)

    username = " "
    while True:
        username = input("Welcome! Please enter your name: \n")

        if username.isalnum() is not True:
            print(TextColors.RED + "Error: Letters and numbers"
                  "only.\n" + TextColors.WHITE)

        else:
            print(f"\nHi {TextColors.BLUE}{username}!" + TextColors.WHITE)
            print("You have up to" + TextColors.BLUE + " 6 "
                  + TextColors.WHITE + "guesses to guess the Word.")
            print("If you have not guessed the word correctly by the time ")
            print("your lives reaches" + TextColors.BLUE + " 0, "
                  + TextColors.WHITE + "it is game over.\n")
            input("When ready to play, press" + TextColors.BLUE + " Enter, \n"
                  + TextColors.WHITE)
            return username


def get_random_word():
    """
    Picks a random word from words.txt to be used as the word the player has
    to guess.
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    return random_word.upper()


def play_game(word):
    """
    Function to play game
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 6
    print("Let's play Hangman!")
    print(display_hangman(lives))
    print("\n")

    if lives > 0:
        print(f"Lives: {lives}\n")
        print("The word to guess: " + " ".join(word_completion) + "\n")
        print("Letters guessed: " + ", ".join(sorted(guessed_letters)) + "\n")

    while not guessed and lives > 0:
        guess = input("Please guess a letter or word: \n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(TextColors.YELLOW + f"You already guessed the"
                      f" letter {guess} \n" + TextColors.WHITE)
                print("The word to guess: " + " ".join(word_completion) +
                      "\n")
                print("Letters guessed: " +
                      ", ".join(sorted(guessed_letters)) + "\n")

            elif guess not in word:
                print(TextColors.RED + f"{guess} is not in the"
                      f" word. Lives left: {lives} \n" + TextColors.WHITE)
                lives -= 1
                guessed_letters.append(guess)
                print(display_hangman(lives))
                print("The word to guess: " + " ".join(word_completion) +
                      "\n")
                print("Letters guessed: " +
                      ", ".join(sorted(guessed_letters)) + "\n")

            else:
                print(TextColors.GREEN + f"Good job, {guess} is in the"
                      " word!\n" + TextColors.WHITE)
                guessed_letters.append(guess)
                word_completion_list = list(word_completion)
                indices = [i for i, letter in enumerate(word)
                           if letter == guess]
                for index in indices:
                    word_completion_list[index] = guess
                word_completion = "".join(word_completion_list)
                if "_" not in word_completion:
                    guessed = True
                print("The word to guess: " + " ".join(word_completion) +
                      "\n")
                print("Letters guessed: " +
                      ", ".join(sorted(guessed_letters)) + "\n")

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess} \n")
            elif guess != word:
                print(TextColors.RED + f"{guess} is not the word."
                      f"Lives left: {lives}\n" + TextColors.WHITE)
                lives -= 1
                guessed_words.append(guess)
                print(display_hangman(lives))
            else:
                guessed = True
                word_completion = word

        else:
            print(TextColors.RED + "Not a valid guess. \n" + TextColors.WHITE)
            print(display_hangman(lives))
            print(word_completion)
            print("\n")

    if guessed:
        print("Congrats, you guessed"
              + TextColors.BOLD + f" {word}" + TextColors.WHITE +
              " correctly!")
        player_wins()

    else:
        print("Sorry you ran out of tries."
              " The word was" + TextColors.BOLD + f" {word}.")
        game_over()


def player_wins():
    """
    Graphics for when player wins
    """
    print(
            TextColors.GREEN + """
        __   __
        \\ \\ / /__  _   _
         \\ V / _ \\| | | |
          | | (_) | |_| |
          |_|\\___/_\\__,_| _
        __      _(_)_ __ | |
        \\ \\ /\\ / / | '_ \\| |
         \\ V  V /| | | | |_|
          \\_/\\_/ |_|_| |_(_)
        """ + TextColors.WHITE
        )
    restart_game()


def game_over():
    """
    Graphics for game over
    """
    print(
            TextColors.RED + """
          ____
         / ___| __ _ _ __ ___   ___
        | |  _ / _` | '_ ` _ \\ / _ \\
        | |_| | (_| | | | | | |  __/
         \\____|\\__,_|_| |_| |_|\\___|
         / _ \\__   _____ _ __| |
        | | | \\ \\ / / _ \\ '__| |
        | |_| |\\ V /  __/ |  |_|
         \\___/  \\_/ \\___|_|  (_)
        """ + TextColors.WHITE
        )


def display_hangman(lives):
    """
    Illustrations of a man being hanged displayed as
    the game goes on
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[lives]


def restart_game():
    """
    Restart game function
    """
    game_restart = False
    while not game_restart:
        restart = input(f"Would you like to play again? {TextColors.BLUE}"
                        f"Y/N{TextColors.WHITE}\n ").upper()
        try:
            if restart == "Y":
                game_restart = True
                welcome_to_game()
                word = get_random_word()
                play_game(word)

            elif restart == "N":
                game_restart = True
                print(TextColors.BLUE + "\nThank you for playing! Take care"
                      " until next time! \n" + TextColors.WHITE)

            else:
                raise ValueError(
                    f" You must type in Y or N. You typed {(restart)}"
                )

        except ValueError as e:
            print(f"{TextColors().RED}{e}.\n Please try again.\n"
                  f"{TextColors().WHITE}")


def main():
    """
     The main function to call all other functions
    """
    welcome_to_game()
    word = get_random_word()
    play_game(word)
    restart_game()


if __name__ == "__main__":
    main()
