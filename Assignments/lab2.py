list = []
for i in range(1, 6):
    num = int(input(f"Enter number {i}: "))
    list.append(num)
print(list)

total = 0
Maximum = list[0]
minimum = list[0]
Even = 0
Odd = 0
for num in list:
    total += num
    if num > Maximum:
        Maximum = num
    if num < minimum:
        minimum = num

    if num % 2 == 0:
        Even +=1
    if num % 2 != 0:
        Odd += 1

print(f"Total: {total}")
print(f"Max: {Maximum}")
print(f"Min: {minimum}")
print(f"Even: {Even}")
print(f"Odd: {Odd}")

