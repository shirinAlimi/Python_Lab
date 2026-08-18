marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 91,
    "Emma": 55
}

total = 0
count = 0
highest = None
highest_students = []

for name, mark in marks.items():
    print(name, ":", mark)

    total += mark
    count += 1

    if highest is None or mark > highest:
        highest = mark

average = total / count

for name, mark in marks.items():
    if mark == highest:
        highest_students.append(name)

print("\nClass average:", average)
print("Highest mark:", highest)
print("Student(s) with highest mark:")

for name in highest_students:
    print(name)

print("Students scoring at least 60:")

for name, mark in marks.items():
    if mark >= 60:
        print(name)