############DEBUGGING#####################


# Describe Problem
def my_function():
    # i will never reach 20 with range(1, 20)
    # for i in range(1, 20):
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()


# Reproduce the Bug
from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# randint(1, 6) produces a random number between 1 - 6 inclusive
# What we want is 0 - 5 to match dice_imgs indexes
# dice_num = randint(1, 6)
#
# Set dice_num to 6 to be able to reproduce the bug consistently
# dice_num = 6
dice_num = randint(0, 5)
print(dice_imgs[dice_num])


# Play Computer
year = int(input("What's your year of birth?"))
# These if statements don't cater year == 1994
if year > 1980 and year < 1994:
    print("You are a millenial.")
# elif year > 1994:
elif year >= 1994:
    print("You are a Gen Z.")


# Fix the Errors
age = input("How old are you?")
# Can't compare a string with an int
# if age > 18:
if int(age) > 18:
    # {age} isn't replaced because we're not printing an f-string
    # print("You can drive at age {age}.")
    print(f"You can drive at age {age}.")


# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# Double equals produces True or False, 1 or 0
# word_per_page == int(input("Number of words per page: "))
word_per_page = int(input("Number of words per page: "))
# Print pages and word_per_page to see their values
# print(pages)
# print(word_per_page)
total_words = pages * word_per_page
print(total_words)


# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    # b_list is only appended once after the loop has completed
    # b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
