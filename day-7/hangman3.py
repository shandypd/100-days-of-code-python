import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = ["_"] * len(chosen_word)

guessed = False
while not guessed:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    guessed = "_" not in display

    print(display)
