size = int(input("Enter the size of the array: "))
array = []
print("Enter the elements of the array:")
for i in range(size):
    element = int(input())
    array.append(element)
elements = 0
for num in array:
    elements += num
print("Sum of elements in the array:", elements)
