import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
    """,
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
    """,
    """
  +---+
  |   |
      |
      |
      |
      |
=========
    """,
]
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = ["_"] * len(chosen_word)
game_over = False
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1

    print(stages[lives])
    print(display)

    game_over = ("_" not in display) or (lives == 0)

if lives > 0:
    print("You win!")
else:
    print("You lose")
