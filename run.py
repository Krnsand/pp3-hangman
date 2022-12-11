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
# data = scores.get_all_values()
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
            print(f"\nHi {username}, You have up to 6 guesses to guess the Word.")
            print("If you have not guessed the word correctly by the time ")
            print("your lives reaches 0, it is game over.\n")
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


def play_game(word):
    """
    Function to play game
    """
    # word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 6
    print("Let's play Hangman!")
    print(display_hangman(lives))
    print(word_completion)
    print("\n")
    while not guessed and lives > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed letter {guess}")

            elif guess not in word:
                print(f"{guess} is not in the word.")
                lives -= 1
                guessed_letters.append(guess)

            else:
                print(f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                lives -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess.")
            print(display_hangman(lives))
            print(word_completion)
            print("\n")
    if guessed:
        print("Congrats, you guessed the word! You Win!")
    else:
        print(f"Sorry you ran out of tries. The word was {word}.")


def display_hangman(lives):
    """
    Illustrations of a man being hanged displayed as the game goes on
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


def main():
    """
    The main function to call all other functions
    """
    welcome_to_game()
    word = get_random_word()
    play_game(word)
    while input("Do you want to play again? Press Y/N \n").lower() == "y":
        welcome_to_game()
        word = get_random_word()
        play_game(word)
        break
    else:
        print("Thank you for playing! Take care until next time!")


if __name__ == "__main__":
    main()

"""
welcome_to_game()
get_random_word()
restart_game()
play_game()
"""

