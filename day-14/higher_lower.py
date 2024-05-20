from art import logo, vs
from game_data import data
from random import shuffle
import os

A = 0
B = 1


def get_item_string(item):
    return f"{item['name']}, a {item['description']}, from {item['country']}"


def get_player_guess():
    while True:
        guess = input("Who has more followers? (A/B): ").lower()

        if guess == "a":
            return A
        elif guess == "b":
            return B


def game():
    shuffle(data)

    items = {A: data.pop(), B: data.pop()}
    score = 0
    game_over = False

    while True:
        os.system("clear")

        print(logo)

        if game_over:
            print(f"Sorry, that's wrong. Final score: {score}.\n")
            break

        if score > 0:
            print(f"You're right! Current score: {score}.\n")

        print(f"Compare A: {get_item_string(item=items[A])}.")
        print(vs)
        print(f"Against B: {get_item_string(item=items[B])}.\n")

        guess = get_player_guess()

        followers_guess = items[guess]["follower_count"]
        followers_other = items[int(not guess)]["follower_count"]

        if followers_guess >= followers_other:
            score += 1
            items[A] = items[B]
            items[B] = data.pop()
        else:
            game_over = True


game()
