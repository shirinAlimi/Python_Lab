numbers = [1, 2, 3, 4, 5]

# reverse() reverses the list in-place and modifies the original list
numbers.reverse()
print(numbers)


# slicing [::-1] creates a new reversed list without changing the original
reversed_list = numbers[::-1]
print(reversed_list)