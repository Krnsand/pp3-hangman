# **Hangman**
This is a classic Hangman game which in this case is a Python terminal game. It runs on the Code Institute mock terminal on Heroku written entirely in python code.
The player can guess a letter or word until the word is completed or until they run out of lives.
My target audience is anyone who wants to play a game. Programmers might find the termial environment more intriguing, but I have used colors for an easier read for anyone not used with a terminal view like this. 

[Hangman](https://pp3-hangman1.herokuapp.com/) - You can view the live site here. 

![Am I Responsive?](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/am_i_responsive.png) 

--- 

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

--- 

 ## **How to Play**
 Players are trying to guess a secret word. The word is randomly chosen and prints in the mock teriminal as _ _ _ _ _ depending on how many letters are in the word. With each correct guess the player can see where in the word the letter is placed. The player can guess entire words if they think they know it. With each wrong guess of letter or word, a life is lost. When the player runs out of lives it is game over.

 ## **Planning Stage**

 ### **User Goals**
 * My goal was to build a terminal version of Hangman to play when one wants to take a break from work or studying.
    * The game should be easy to play.
    * The game should be fun to play.
    * There should be some level of challenge for the user to keep them coming back.

 ### **Using FlowCharts**
 * I used a flowchart to plan my project to give myself a clear structure of what I wanted to incorporate
    * What steps are needed for the basics of the game?
    * What happens if an invalid character is played?
    * Does the player want to play again?

 ![Design FlowChart](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/flowchart.png)

--- 

 ## **Features**

 ### **Existing Features**
 * **Welcome to the game**
    * Here the player gets welcomed to the game
    * They are asked to enter their name (for the scoreboard)
    * Once a name is entered the player gets to see the rules and after that the game begins

![Welcome to game](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/welcome_user.png)

* **Letters and numbers only**
    * Here the player has used an invalid character (' ! ') which is shown with red text
    * The player is prompted to enter a new name

![Letter and numbers only](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/lets_and_numbs.png)

 * **Start game**
    * Here the player gets a visual of the gallows that will build with each wrong guess
    * They can see how many lives they will start out with
    * How many letters the word to guess is comprised of
    * Which letters have already been guessed (in this image there are no letters as it is at the start of the game and no guess has been made)
    * A prompt to enter a letter

![Start game](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/start_game.png)

 * **Correct guess**
    * Here the player gets a message that the letter they guessed is in the word
    * This is green as a visual feedback that it is a correct guess
    * The guessed letter is placed at the correct placement in the word
    * The guessed letter is also placed in the "Letters guessed" field

![Correct guess](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/correct_guess.png)

 * **Not a valid guess**
    * Here the player has made an invalid guess (' ! ') which is shown with red text
    * The player is prompted to make a new guess

![Not valid guess](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/not_valid.png)

* **Wrong guess**
    * Here the player gets a message that the letter they guessed is not in the word
    * This is red as a visual feedback that it is an incorrect guess
    * The amount of lives is shown so the player can know how many guesses they have left
    * The guessed letter is also placed in the "Letters guessed" field

![Wrong guess](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/wrong_guess.png)

* **Repeated guess**
    * Here the player gets a message that the letter they just guessed has already been guessed
    * This is yellow as a visual feedback to alert the player that somethng is wrong but not wrong enough to loose a life
    * The player is prompted to make a new guess

![Repeated guess](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/repeated_guess.png)

* **You win!**
    * The player has guessed the word correctly and is rewarded with graphics printed in the terminal
    * The graphics is green as a visual feedback for success
    * The final score is printed. If the player decides to play again the score will continue to add or subtract until the player no longer wants to play again
    * The player is asked if they would like to play again

![You win](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/you_win.png)

* **Play again**
    * Here the player has chosen Y (YES)
    * The player can see their final score for this round
    * The game restarts 

![Play again](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/play_again.png)

* **Game over**
    * The player has run out of lives without guessing the word, a graphics is printed in the terminal
    * The graphics is red as a visual feedback for failure
    * The final score is printed. If the player decides to play again the score will continue to add or subtract until the player no longer wants to play again
    * The player is asked if they would like to play again

![Game over](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/game_over.png)

* **Error message**
    * The player has written H instead of Y/N
    * An error message in red tells the player what is wrong
    * The player is asked to try again

![Error message](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/y_or_n.png)

* **Thanks for playing**
    * Here the player has chosen N (NO) and the game stops
    * The final score is printed and added to the scoreboard in the google spreadsheet

![Thanks for playing](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/thanks_for_playing.png)

* **Scoreboard**
    * All the players scores are calculated and compiled into a google spreadsheet 

![Scoreboard](https://github.com/Krnsand/pp3-hangman/blob/main/assets/images/scores.png)

 ## **Future Features**
  * I would like to add a possibility to choose a difficulty for the player. Where an easy setting would give an easier/more common or shorter word, and a more difficult setting would give a longer and less common word
  * I would like to add a leaderboard where players can see what other players have gotten and in that way play against each other

--- 

 ## **Testing**
  * I have tested the code using a Linter that has shown errors and warnings in the code continuously, allowing me to fix them right away
  * I have tested the code throughout my progress in the Gitpod terminal to make sure that the code is doing what I want it to do
  * I have tested the code in my deployed version to make sure that it does the same thing as in the Gidpod termial
  * I have asked friends to try it to make sure the game layout makes sense and that it is intuitive, even for a non programmer
  * I have exercised defensive programming in the way that I have tried to break my program by inputting wrong characters, inputting nothing or repeating guesses, and printing an error message each time. See images in <b>Letters and numbers only</b>, <b>Not a valid guess</b>, <b>Wrong guess</b>, <b>Repeated guess</b>, <b>Error message</b>
---

 ## **Technologies Used**
 * **Languages**
    * Python.

 * **Libraries**
    * random to select a random word
    * gspread for my google sheet with the scores
    * credentials 

 * **Other**
    * The Code Institute's GitHub full template for Python to start the project
    * A generator to create randomly generated words for my words.txt, taken from (https://www.randomlists.com/random-words)
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
    * GitHub is used to store the projects code after being pushed from Git.
    * Heroku is used to build, run and scale applications in a similar manner across most languages.

---

 ## **Bugs**

 ### **Fixed Bugs**
  * First I could not get get_random_word to work with random.choice, but after having tried a couple of different methods I finally managed to fix that. See commit 87a3ca1 for final code on that point
  * I struggled for a long time to get the scores calculated and exported to my google spreadsheet. My mentor helped me with debugging here and we managed to get that working. See commit a5c902f
  * It took me a while to get the lives to count down correctly, but after a discussion with my friend I got it to work. See commit ab4c053

 ### **Unfixed Bugs**
 One bug I have found is sometimes when I test the game on a mobile device, all my input data is shown each time I make a new input. See bottom of image. I have not experienced that this makes the game not work, but it does not make for a pleasant user experience. I don't know why this happens on mobile devices but I will look into it in the fututre

<details><summary>Mobile bug</summary>
  <img src="https://github.com/Krnsand/pp3-hangman/blob/main/assets/bug.png">
  </details>

 ---

 ## **Validators**
 I have validated my code throughout the progress of my project thanks to a pre-installed Linter in the python essentials template 

 ---

 ## **Deployment**
 * To deploy this project I had to
    * Create a new app in Heroku
    * Add Config Var's for Creds and Port
    * Add buildpacks for python and nodeJS
    * Connect to Github
    * Link the Heroku app to project repository
    * Enable automatic deploys 
    * Deploy manually
---

 ## **Credits**
 * I used [Am I Responsive?](https://ui.dev/amiresponsive) for my starting image
 * I used [Lucid Charts](https://lucid.app/users/login#/login) to make my flowchart
 * I used [Love Sandwiches](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/) to get the APIs for my spreadsheet, credentials and scope for the project
 * I used [ASCII Art Generator](http://patorjk.com/software/taag/#p=display&f=Doom&t=Type%20Something%20) for my graphics in the game
 * I used a video by [Kite](https://www.youtube.com/watch?v=m4nEnsavl6w) for the core game code, and then altered it/added to it to work the way I wanted with other features. I also used the illustrations of the hanged man
 * I took inspiration from [gibbo101](https://github.com/gibbo101/hangman/blob/main/README.md) regarding the colored code as well as how to get the random word from my words.txt file
 * I took inspiration from [KeoCode](https://github.com/KeoCode/Hangman) regarding the welcome message
 * I used [Ozzmaker](https://ozzmaker.com/add-colour-to-text-in-python/) to understand how to write colored code

 ### **Thanks**
  * I would like to thank my mentor André Aquilina for helping me throughout the progress with my project. He helped me figure out why my scores were not transfering to my google sheet 

---
  