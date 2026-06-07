matrix = []

print("Enter the elements of a 3x3 matrix: ")
for i in range(3):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix.append(row)

# Row sums
print("\nRow sums:")
for i in range(3):
    row_sum = 0
    for num in matrix[i]:
        row_sum += num
    print("Row", i+1, "=", row_sum)

# Column sums
print("\nColumn Sums: ")
for j in range(3):
    column_sum = 0
    for i in range(3):
        column_sum += matrix[i][j]
    print("Column", j + 1, "=", column_sum)

# Total sum
total = 0
for i in range(3):
    for j in range(3):
        total += matrix[i][j]

print("\nTotal sum =", total)