from art import logo
from helper import (
    build_deck,
    get_card_labels,
    get_cards_total_value,
    print_game_result,
    want_to_play,
    want_to_get_another_card,
)
import os

print(logo)

while want_to_play():
    os.system("clear")

    deck = build_deck()

    player_cards = [deck.pop(), deck.pop()]
    dealer_cards = [deck.pop(), deck.pop()]

    player_score = 0

    while True:
        print(logo)

        player_score = get_cards_total_value(player_cards)

        print(f"Your cards: {get_card_labels(player_cards)}, score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]['label']}\n")

        if want_to_get_another_card(player_score):
            player_cards.append(deck.pop())

            os.system("clear")
        else:
            break

    dealer_score = 0
    while True:
        dealer_score = get_cards_total_value(dealer_cards)
        if dealer_score < 17:
            dealer_cards.append(deck.pop())
        else:
            break

    print(f"Dealer's cards: {get_card_labels(dealer_cards)}, score: {dealer_score}\n")

    print_game_result(player_score, dealer_score)
