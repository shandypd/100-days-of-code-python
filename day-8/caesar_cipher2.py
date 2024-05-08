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


def encrypt(text, shift):
    result = ""

    for char in text:
        if char in alphabet:
            index = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[index]
        else:
            result += char

    print(f"The encoded text is {result}")


def decrypt(text, shift):
    result = ""

    for char in text:
        if char in alphabet:
            index = (len(alphabet) + alphabet.index(char) - shift) % len(alphabet)
            result += alphabet[index]
        else:
            result += char

    print(f"The decoded text is {result}")


if direction == "encode":
    encrypt(text=text, shift=shift)
elif direction == "decode":
    decrypt(text=text, shift=shift)
else:
    print('Unknown direction, please type "encode" or "decode"')
