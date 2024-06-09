string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if len(string1) != len(string2):
    print("The strings are not equal.")
else:
    equal = True
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            equal = False
            break
    if equal:
        print("The strings are equal.")
    else:
        print("The strings are not equal.")
