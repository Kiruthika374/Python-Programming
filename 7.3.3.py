string = input("Enter a string of binary characters: ")

decimal = 0

for char in string:

    decimal = decimal * 2 + int(char)


if decimal % 3 == 0:
    print("The binary string is a multiple of 3.")
else:
    print("The binary string is not a multiple of 3.")
