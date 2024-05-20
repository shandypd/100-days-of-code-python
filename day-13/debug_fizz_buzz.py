# Target is the number up to which we count
target = int(input())
for number in range(1, target + 1):
    # FizzBuzz should be printed for a number divisible by both 3 and 5, not only one of them
    # if number % 3 == 0 or number % 5 == 0:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Change to elif so that we only print one result for each number
    # if number % 3 == 0:
    elif number % 3 == 0:
        print("Fizz")
    # if number % 5 == 0:
    elif number % 5 == 0:
        print("Buzz")
    else:
        # Remove square bracket to print an integer
        # print([number])
        print(number)
