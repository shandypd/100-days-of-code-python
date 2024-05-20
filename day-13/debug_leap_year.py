# Which year do you want to check?
# year = input()
year = int(input())

# TypeError, can't perform modulus on a string
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
