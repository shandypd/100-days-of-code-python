# Get a character at certain index from a string
print("Hello"[4])

# Integer
print(100)

# Integer with thousands separator
print(123_456_789)

# Float
print(3.14159)

# Boolean
print(True)
print(False)

# Get data type
print(type(7))

# A string can only be concatenated with another string
# Use str() function to convert a value to a string
num_char = len(input("What is your name? "))
print("Your name has " + str(num_char) + " characters.")

# Or use the f-string
print(f"Your name has {num_char} characters.")

# Division always produces a float
print(type(6 / 3))

# Floor division
print(8 // 3) # =2

# Power operator
print(2 ** 2) # =4

# Round float
print(round(2.666666, 2))

# Format float to always show 2 decimal places
print("{:.2f}".format(2.6))
