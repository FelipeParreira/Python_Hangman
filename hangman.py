from random import randint

def play_round():
  words = ["3dhubs", "marvin", "print", "filament", "order", "layer"]
  random_index = randint(0, len(words) - 1)
  random_word = words[random_index]
  guesses = 5
  guessed_letters = []
  displayed_word = ["_"] * len(random_word)

  indexes = {}
  for index in range(0, len(random_word)):
    letter = random_word[index]
    if not (letter in indexes):
      indexes[letter] = []
    indexes[letter].append(index)

  while guesses > 0:
    if len(indexes) == 0:
      print("Congratulations! You won!")
      return len(random_word) - (5 - guesses)

    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in guessed_letters:
      print("You already guessed this letter. Please, try again.")
      continue

    guessed_letters.append(guessed_letter)

    if guessed_letter in indexes:
      for index in indexes[guessed_letter]:
        displayed_word[index] = guessed_letter.upper()
      del indexes[guessed_letter]
    else:
      guesses -= 1
      print("Wrong guess :(")
    
    print(" ".join(displayed_word))
  
  if guesses == 0:
    print("You lost :(")
    return 0

def play_game():
  should_game_continue = input("Do you want to play hangman [y/N]? ").lower()[0] == 'y'
  highest_score = 0

  while should_game_continue:
    highest_score = max(highest_score, play_round())
    print("Your highest score so far is %d" % highest_score)
    should_game_continue = input("Do you want to play another round [y/N]? ").lower()[0] == 'y'

  print("Your highest score was %d" % highest_score)
  print("Bye, bye. Hope to see you again...")

play_game()