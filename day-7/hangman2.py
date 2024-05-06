import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"The solution is {chosen_word}")

display = ["_"] * len(chosen_word)

guess = input("Guess a letter: ").lower()

for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess

print(display)
