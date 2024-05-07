import os
import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)

display = ["_"] * len(chosen_word)
game_over = False
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    os.system("clear")

    if guess in display:
        print(f'You have guessed "{guess}".')

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        print(f'letter "{guess}" is not in the word.')
        lives -= 1

    print(stages[lives])
    print(f"{display}\n")

    game_over = ("_" not in display) or (lives == 0)

if lives > 0:
    print("You win!")
else:
    print(f'You lose, the word is "{chosen_word}"')
