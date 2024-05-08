from art import logo


def caesar(text, shift, direction):
    if direction == "decode":
        shift *= -1

    result = ""

    for char in text:
        char_code = ord(char)

        offset = 0
        if char_code >= 65 and char_code <= 90:
            offset = 65
        elif char_code >= 97 and char_code <= 122:
            offset = 97

        new_char_code = char_code
        if offset > 0:
            new_char_code = (26 + char_code - offset + shift) % 26 + offset

        result += chr(new_char_code)

    print(f"The {direction}d text is {result}")


print(logo)

end = False
while not end:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))

        caesar(text=text, shift=shift, direction=direction)
    else:
        print("Invalid input.")

    start_over = input('Type "yes" to go again:\n')
    if start_over.lower() != "yes":
        end = True
