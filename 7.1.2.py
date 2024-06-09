string = input("Enter a string: ")
replace = input("Enter the character to replace: ")
replacement = input("Enter the replacement character: ")
modified = ""
flag = False
for char in string:
    if char == replace and not flag:
        modified += replacement
        flag = True
    else:
        modified += char
print("Modified string:", modified)