n = int(input("Enter the number of elements in the array: "))
array = []

print("Enter the elements of the array:")
for i in range(n):
    element = int(input())
    array.append(element)
total = 2 ** n
print("Total number of subsets:", total)
