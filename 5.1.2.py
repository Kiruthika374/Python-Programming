
array = [10, 20, 30, 40, 50]
element = int(input("Enter the element to search: "))
found = False
for i in range(len(array)):
    if array[i] == element:
        print("Element found at position:", i)
        found = True
        break
if not found:
    print("Element not found in the array.")
