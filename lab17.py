matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#Entire matrix
for row in matrix:
    print(row)

#First row
print("First row: ", matrix[0])

#last column
last_column = [row[-1] for row in matrix]
print("last column: ", last_column)

total = 0
for row in matrix:
    for num in row:
        total += num
print("Total: ", total)