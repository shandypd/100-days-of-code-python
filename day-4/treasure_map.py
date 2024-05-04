line1 = ["□", "□", "□"]
line2 = ["□", "□", "□"]
line3 = ["□", "□", "□"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()

x = ord(position[0].upper()) - 65
y = int(position[1]) - 1
map[y][x] = "X"

print(f"{line1}\n{line2}\n{line3}")
