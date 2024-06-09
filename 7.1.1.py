string = input("Enter a string: ")
freq = {}
for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print("Frequency of each character in the string:")
for char, freq in freq.items():
    print(char, ":", freq)
