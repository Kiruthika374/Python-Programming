string = input("Enter a string: ")
compressed = ""
current = string[0]
count = 1
for i in range(1, len(string)):
    if string[i] == current:
        count += 1
    else:
        compressed += current + str(count)
        current = string[i]
        count = 1
        
compressed += current + str(count)

if len(compressed) < len(string):
    print("Compressed string:", compressed)
else:
    print("Compressed string is not shorter than the original string. Original string:", string)
