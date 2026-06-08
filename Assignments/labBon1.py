numbers = list(map(int, input("Enter numbers: ").split()))

largest = second = float("-inf")

for n in numbers:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second largest =", second)