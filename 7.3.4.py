string = input("Enter a string: ")


lowercase = ""
for char in string:
    
    if 'A' <= char <= 'Z':
        
        lowercase += chr(ord(char) + 32)
    else:
        
        lowercase += char
print("Lowercase string:", lowercase)
