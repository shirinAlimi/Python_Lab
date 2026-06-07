# Numbers from 1 to 20
numbers = [x for x in range(1, 21)]
print(numbers)

# Even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

odd = [x for x in range(1, 21) if x % 2 != 0]
print(odd)

# Squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)