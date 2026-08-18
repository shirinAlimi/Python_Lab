number = int(input("Enter a positive integer: "))

original = number
digit_count = 0
digit_sum = 0
reversed_number = 0

while number > 0:
    digit = number % 10

    digit_count += 1
    digit_sum += digit
    reversed_number = reversed_number * 10 + digit

    number //= 10

print("Number of digits:", digit_count)
print("Sum of digits:", digit_sum)
print("Reversed number:", reversed_number)