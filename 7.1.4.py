
def leng(string):
    length = 0
    for char in string:
        length += 1
    return length
def copy(string):
    copy = ""
    for char in string:
        copy += char
    return copy
def concatenate(string1, string2):
    concatenated = string1 + string2
    return concatenated
def uppercase(string):
    uppercase = ""
    for char in string:
        if 'a' <= char <= 'z':
            uppercase += chr(ord(char) - 32)
        else:
            uppercase += char
    return uppercase
def compare(string1, string2):
    if string1 < string2:
        return -1
    elif string1 == string2:
        return 0
    else:
        return 1
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

print("Length of string 1:", leng(string1))
print("Copy of string 1:", copy(string1))
print("Concatenation of string 1 and string 2:",concatenate(string1, string2))
print("Uppercase conversion of string 1:", uppercase(string1))
print("Comparison result of string 1 and string 2:", compare(string1, string2))
