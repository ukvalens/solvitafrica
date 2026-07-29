
numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

average = sum(numbers) / len(numbers)

print("Numbers entered:", numbers)
print("Average =", average)