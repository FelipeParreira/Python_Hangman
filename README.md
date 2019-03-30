# Hangman
This is a CLI Hangman game, built with Python.

## Game rules
1. The game chooses a random word out of 6 words: `['3dhubs', 'marvin', 'print', 'filament', 'order', 'layer']`;
2. The spaces for the letters of the word are displayed (e.g.: `'​_ _ _​ _ _'` for `'order'`);
3. The user can choose a letter and if that letter exists in the chosen word it is shown on the puzzle (e.g.: asks for `'r'` and now it shows `'​_ r _​ _ r'` for `'order'`);
4. The user can only ask 5 letters that don't exist in the word and then it's game over;
5. If the user wins, (s)he is congratulated and their highest score so far is saved and displayed
6. The score is the number of characters in a word minus the number of wring guesses (if the user loses a round, the score is 0).

## How to get it running
1. Download or clone the repo to your local machine;
2. Navigate to the root folder of the repo using the command line;
3. Run `python3 hangman.py`;
4. Have fun!

** P.S.: You need to have `Python 3` installed in your machine.
