import random

EASY = "easy"
HARD = "hard"
EASY_MAX_ATTEMPTS = 10
HARD_MAX_ATTEMPTS = 5
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_difficulty_input():
    while True:
        difficulty = input(f"Choose a difficulty. ({EASY}/{HARD}): ").lower()

        if difficulty == EASY or difficulty == HARD:
            return difficulty


def get_max_attempts(difficulty):
    if difficulty == EASY:
        return EASY_MAX_ATTEMPTS
    elif difficulty == HARD:
        return HARD_MAX_ATTEMPTS
    else:
        print(f"Invalid difficulty arg, possible values are: {EASY}, {HARD}")
        return 0


def get_random_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def main():
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")

    difficulty = get_difficulty_input()
    attempts_left = get_max_attempts(difficulty=difficulty)
    number_to_guess = get_random_number()
    guess = None

    while attempts_left > 0:
        print(f"You have {attempts_left} attempt(s) remaining to guess the number.")

        guess = int(input("Make a guess: "))

        if guess > number_to_guess:
            print("Too high.")
        elif guess < number_to_guess:
            print("Too low.")
        else:
            break

        attempts_left -= 1

        if attempts_left > 0:
            print("Guess again.")

    if number_to_guess == guess:
        print(f"You got it! The answer was {number_to_guess}.")
    else:
        print("You've run out of guesses, you lose.")


main()
