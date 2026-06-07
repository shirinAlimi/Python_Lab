list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
for i in list:
    if i % 2 == 0:
        print(i)
found = False
num = int(input("Enter a number: "))
for i in range(len(list)):
    if list[i] == num:
        print("Number found")
        print(i)
        found = True
        break
if not found:
    print("Number not found")