
n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    element = int(input())
    arr.append(element)
print("Elements of the array:")
for element in arr:
    print(element)
