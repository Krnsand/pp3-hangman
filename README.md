# **Hangman**
This is a classic Hangman game which in this case is a Python terminal game. It runs on the Code Institute mock terminal on Heroku written entirely in python code.
The player can guess a letter or word until the word is completed or until one runs out of lives.
My target audience is anyone who wants to play a game. Programmers might find the termial environment more intriguing, but I have used colors for an easier read for anyone not used with a terminal like this. 

[Hangman](https://pp3-hangman1.herokuapp.com/) - You can view the live site here. 

![Am I Responsive?](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/am_i_responsive.png) 

## **Table of Contents**
 * [**How to Play**](#how-to-play)
 * [**Planning Stage**](#planning-stage)
   * User Goals
   * Using FlowCharts
 * [**Features**](#features)
   * Future Features
 * [**Testing**](#testing)
 * [**Technologies Used**](#technologies-used)
 * [**Bugs**](#bugs)
   * Fixed Bugs
   * Unfixed Bugs
 * [**Validators**](#validators)
 * [**Deployment**](#deployment)
 * [**Credits**](#credits)
   * Thanks

 ## **How to Play**

 ## **Planning Stage**

 ### **User Goals**

 ### **Using FlowCharts**
 ![Design FlowChart](docs/read-me/hangman-flowchart.png)

 ## **Features**

 ### **Existing Features**
 * Welcome to the game
    * Here the player gets welcomed to the game
    * They are asked to enter their name (for the scoreboard)
    * Once a name is entered the player gets to see the rules and after that the game begins

![Welcome to game](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/welcome_user.png)

* Letters and numbers only
    * Here the player has used an invalid character (' ! ') which is shown with red text
    * The player is prompted to entera new name

![Letter and numbers only](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/lets_and_numbs.png)

 * Start game
    * Here the player gets a visual of the gallows that will build with each wrong guess
    * They can see how many lives they will start out with
    * How many letters the word to guess is comprised of
    * Which letters already guessed (in this image there are no letters as it is at the start of the game and no guess has been made)
    * And a prompt to enter a letter

![Start game](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/start_game.png)

 * Correct guess
    * Here the player gets a message that the letter they guessed is in the word
    * This is green as a visual feedback that it is a correct guess
    * The guessed letter is placed at the correct placement in the word
    * The guessed letter is also placed in the "Letters guessed" field

![Correct guess](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/correct_guess.png)

 * Not a valid guess
    * Here the player has made an invalid guess (' . ') which is shown with red text
    * The player is prompted to make a new guess

![Not valid guess](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/not_valid.png)

* Wrong guess
    * Here the player gets a message that the letter they guessed is not in the word
    * This is red as a visual feedback that it is an incorrect guess
    * The amount of lives is shown so the player can know how many guesses they have left
    * The guessed letter is also placed in the "Letters guessed" field

![Wrong guess](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/wrong_guess.png)

* Repeated guess
    * Here the player gets a message that the letter they just guessed has already been guessed
    * This is yellow as a visual feedback to alert the player that somethng is wrong but not wrong enough to loose a life
    * The player is prompted to make a new guess

![Repeated guess](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/repeated_guess.png)

* You win!
    * The player has guessed the word correctly and is rewarded with graphics printed
    * The graphics is green as a visual feedback for success
    * The player is asked if they would like to play again

![You win](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/you_win.png)

* Play again
    * Here the player has chosen Y (YES) and the game restarts 

![Play again](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/play_again.png)

* Game over
    * The player has run out of lives without guessing the word, a graphics is printed
    * The graphics is red as a visual feedback for failure
    * The player is asked if they would like to play again

![Game over](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/game_over.png)

* Thanks for player
    * Here the player has chosen N (NO) and the game stops

![Thanks for playing](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/thanks_for_playing.png)

 ## **Future Features**
  * I would like to add a possibility to choose a difficulty for the player. Where an easy setting would give an easier or shorter word, and a more difficult setting would give a longer and less common word
  * I would like to add a leaderboard where players can play for points and see what other players have gotten and in that way play against each other in a way   

 ## **Testing**
 

 ## **Technologies Used**

 ## **Bugs**

 ### **Fixed Bugs**

 ### **Unfixed Bugs**

 ## **Validators**

 ## **Deployment**

 ## **Credits**

 ### **Thanks**