from art import logo
import os

print(logo)

bid_amounts = {}
highest_bid = 0

end = False
while not end:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))

    bidders = bid_amounts.get(bid, [])
    bidders.append(name)
    bid_amounts[bid] = bidders

    if bid > highest_bid:
        highest_bid = bid

    more_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if more_bidders == "yes":
        os.system("clear")
    else:
        end = True

print(f"The winner is {bid_amounts[highest_bid][0]} with a bid of ${highest_bid}")
