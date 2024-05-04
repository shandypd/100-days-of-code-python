print("The Love Calculator is calculating your score...")

name1 = input()
name2 = input()

combined_name = (name1 + name2).upper()

first_digit = combined_name.count("T")
first_digit += combined_name.count("R")
first_digit += combined_name.count("U")
first_digit += combined_name.count("E")

second_digit = combined_name.count("L")
second_digit += combined_name.count("O")
second_digit += combined_name.count("V")
second_digit += combined_name.count("E")

score = int(f"{first_digit}{second_digit}")

evaluation = ""
if (score < 10) or (score > 90):
    evaluation = ", you go together like coke and mentos."
elif (score >= 40) and (score <= 50):
    evaluation = ", you are alright together."
else:
    evaluation = "."

print(f"Your score is {score}{evaluation}")
