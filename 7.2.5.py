string = input("Enter a string: ")
chars = list(string)
n = len(chars)
for i in range(n):
    for j in range(0, n-i-1):
        if chars[j] > chars[j+1]:
        
            chars[j], chars[j+1] = chars[j+1], chars[j]

sorted = ''.join(chars)

print("Sorted string in alphabetical order:", sorted)
