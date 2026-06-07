numbers = [1, 2, 2, 3, 1, 1]

visited = []

for i in range(len(numbers)):
    if numbers[i] not in visited:
        count = 0

        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                count += 1

        print(numbers[i], "->", count)
        visited.append(numbers[i])