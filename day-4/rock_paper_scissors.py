import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer = random.randint(0, 2)

if player > 2:
    print("You typed an invalid number, you lose")
else:
    print(options[player])
    print(f"Computer chose:\n{options[computer]}")

    if player == 0 and computer == 2:
        print("You win!")
    elif player == 2 and computer == 0:
        print("You lose")
    elif player > computer:
        print("You win!")
    elif player == computer:
        print("It's a draw")
    else:
        print("You lose")
