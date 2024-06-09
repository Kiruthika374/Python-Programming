string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
extra = ''

for char in string2:
    if char not in string1:
    
        extra = char
        break

print("Extra character in the second string:", extra)
