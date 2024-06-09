s= input("Enter a string: ")
k = int(input("Enter the value of k: "))

freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

t = ""

for char in s:
    if freq[char] >= k:
        t += char

print("Largest subsequence with each character occurring at least", k, "times:", t)
