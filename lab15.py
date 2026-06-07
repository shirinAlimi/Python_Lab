numbers = list(map(int, input().split()))

total = 0
largest = numbers[0]
smallest = numbers[0]
for i in numbers:
    total += i

    if i > largest:
        largest = i

    if i < smallest:
        samllest = i
    
Average = total/len(numbers)
print("Total: ", total)
print("Average: ", Average)
print("Largest Number: ", largest)
print("Smallest Number: ", smallest)