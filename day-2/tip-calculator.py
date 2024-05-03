print("Welcome to the tip calculator!")

total = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? ")) / 100
num_people = int(input("How many people to split the bill? "))

each = total * (1 + tip_percentage) / num_people

print(f"Each person should pay: ${'{:.2f}'.format(each)}")
