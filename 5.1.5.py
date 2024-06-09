numbers = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    num = int(input("Enter number {}: ".format(i+1)))
    numbers.append(num)
mean = sum(numbers) / n
deviation = sum((x - mean) ** 2 for x in numbers) / n
variance = deviation ** 0.5
print("Mean:", mean)
print("Deviation:", deviation)
print("Variance:", variance)