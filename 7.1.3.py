string = input("Enter a string: ")
result = ""
for char in string:
    if char not in result:
        result += char
print("String after removing repeated characters:", result)
