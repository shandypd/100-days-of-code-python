for n in range(1, 101):
    output = ""

    if n % 3 == 0:
        output += "Fizz"

    if n % 5 == 0:
        output += "Buzz"

    if output == "":
        output = n

    print(output)
