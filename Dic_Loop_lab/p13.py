while True:
    n = int(input("Enter a positive integer: "))

    if n > 0:
        break

    print("Invalid input. Try again.")

while n >= 1:
    print(n, end=" ")
    n -= 1

print()
print("Launch!")