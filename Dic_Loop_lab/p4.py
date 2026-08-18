n = int(input("Enter a nonnegative integer: "))

factorial = 1
process = ""

for i in range(1, n + 1):
    factorial *= i

    if i == 1:
        process = "1"
    else:
        process += " * " + str(i)

if n == 0:
    print("0! = 1")
else:
    print(process, "=", factorial)