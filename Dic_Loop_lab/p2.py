n = int(input("Enter n: "))

total = 0
count = 0

print("Even numbers:", end=" ")

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
        total += i
        count += 1

print()

if count > 0:
    average = total / count
else:
    average = 0

print("Sum:", total)
print("Average:", average)