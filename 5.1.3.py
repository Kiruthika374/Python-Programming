
n = int(input("Enter the number of elements: "))
numbers = []
print("Enter the numbers:")
for i in range(n):
    number = int(input())
    numbers.append(number)
largest = numbers[0]
smallest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
print("Largest number:", largest)
print("Smallest number:", smallest)

