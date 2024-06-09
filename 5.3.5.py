n = int(input("Enter the number of elements in the array: "))
array = []
print("Enter the elements of the array:")
for i in range(n):
    num = int(input())
    array.append(num)
nonzero = 0
for i in range(n):
    if array[i] != 0:
        array[nonzero] = array[i]
        nonzero +=1
while nonzero < n:
    array[nonzero] = 0
    nonzero += 1
print("Array after moving 0's to the end while maintaining order:", array)
