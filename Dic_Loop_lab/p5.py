n = int(input("Enter an integer greater than 1: "))

is_prime = True
first_divisor = 0

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        first_divisor = i
        break

if is_prime:
    print(n, "is a prime number.")
else:
    print(n, "is not prime. Its first divisor is", first_divisor)