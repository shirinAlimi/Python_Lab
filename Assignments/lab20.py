runs = list(map(int, input("Enter runs in 15 matches: ").split()))

total = 0
highest = runs[0]
lowest = runs[0]

for r in runs:
    total += r

    if r > highest:
        highest = r

    if r < lowest:
        lowest = r

average = total / len(runs)

# Half-centuries and centuries
half_centuries = 0
centuries = 0

for r in runs:
    if r >= 100:
        centuries += 1
    elif r >= 50:
        half_centuries += 1

print("Total runs =", total)
print("Average =", average)
print("Highest score =", highest)
print("Lowest score =", lowest)
print("Half-centuries =", half_centuries)
print("Centuries =", centuries)