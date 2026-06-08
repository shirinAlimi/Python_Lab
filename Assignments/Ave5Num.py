total = 0

for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    total += num

average = total / 5

print("Average =", average)