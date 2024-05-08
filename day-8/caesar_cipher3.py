alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    if direction == "decode":
        shift *= -1

    result = ""

    for char in text:
        if char in alphabet:
            index = (len(alphabet) + alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[index]
        else:
            result += char

    print(f"The {direction}d text is {result}")


caesar(text=text, shift=shift, direction=direction)
