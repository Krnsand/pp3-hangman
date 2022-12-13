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
    print(f"Lives: {lives}\n")
    print("The word to guess: " + " ".join(word_completion) + "\n")
    print("\n")
    while not guessed and lives > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess} \n")

            elif guess not in word:
                print(f"{guess} is not in the word. Lives left: {lives} \n")
                lives -= 1
                guessed_letters.append(guess)
                print(display_hangman(lives))

            else:
                print(f"Good job, {guess} is in the word!\n")
                guessed_letters.append(guess)
                word_completion_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_completion_list[index] = guess
                word_completion = "".join(word_completion_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess} \n")
            elif guess != word:
                print(f"{guess} is not the word. Lives left: {lives}\n")
                lives -= 1
                guessed_words.append(guess)
                print(display_hangman(lives))
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess. \n")
            print(display_hangman(lives))
            print(word_completion)
            print("\n")
    if guessed:
        print("Congrats, you guessed the word! You Win!\n")
    else:
        print(f"Sorry you ran out of tries. The word was {word}.\n")

    print(display_hangman(lives))


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
        print("\nThank you for playing! Take care until next time!")


if __name__ == "__main__":
    main()

"""
welcome_to_game()
get_random_word()
restart_game()
play_game()
"""

