marks = list(map(int, input("Enter marks of 10 students: ").split()))

total = 0
highest = marks[0]
lowest = marks[0]

for mark in marks:
    total += mark

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

# Average
average = total / len(marks)

# Count students above average
count_above_avg = 0
for mark in marks:
    if mark > average:
        count_above_avg += 1

print("Highest mark =", highest)
print("Lowest mark =", lowest)
print("Average mark =", average)
print("Students above average =", count_above_avg)