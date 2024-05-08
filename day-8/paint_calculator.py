from math import ceil


def paint_calc(height, width, coverage):
    cans = height * width / coverage
    print(f"You'll need {ceil(cans)} cans of paint.")


test_h = int(input())
test_w = int(input())
coverage = 5

paint_calc(height=test_h, width=test_w, coverage=coverage)
