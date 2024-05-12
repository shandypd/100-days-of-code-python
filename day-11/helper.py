from random import shuffle


def build_deck(num_of_decks=1):
    suits = ["♠", "♥︎", "♦︎", "♣︎"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    deck = []
    for _ in range(num_of_decks):
        for r in range(len(ranks)):
            value = r + 1
            if r > 9:
                value = 10

            for suit in suits:
                deck.append({"label": f"{ranks[r]}{suit}", "value": value})

    shuffle(deck)

    return deck


def get_card_labels(cards):
    labels = []

    for card in cards:
        labels.append(card["label"])

    return labels


def get_cards_total_value(cards):
    total = 0

    has_ace = False

    for card in cards:
        total += card["value"]

        if card["label"][0] == "A":
            has_ace = True

    if has_ace and total < 12:
        total += 10

    return total


def print_game_result(player_score, dealer_score):
    player_dist = 21 - player_score
    dealer_dist = 21 - dealer_score

    if player_dist < 0:
        print("You went over. You lose 😭.\n")
    elif player_dist == dealer_dist:
        print("Draw 😐.\n")
    elif player_dist == 0:
        print("You have a blackjack. You win 😉!\n")
    elif dealer_dist == 0:
        print("Dealer has a blackjack. You lose 😭.\n")
    elif dealer_dist < 0:
        print("Dealer went over. You win 😉!\n")
    elif player_dist < dealer_dist:
        print("You win 😉!\n")
    else:
        print("You lose 😭.\n")


def want_to_get_another_card(player_score):
    if player_score == 21 or player_score > 21:
        return False

    get_another_card = ""

    while get_another_card != "y" and get_another_card != "n":
        get_another_card = input("Do you want to get another card? (y/n): ")

    print()

    return get_another_card == "y"


def want_to_play():
    play = ""

    while play != "y" and play != "n":
        play = input("Do you want to play a game of Blackjack? (y/n): ")

    return play.lower() == "y"
