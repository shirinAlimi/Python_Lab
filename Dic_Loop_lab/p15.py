correct_pin = "1234"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input("Enter PIN: ")
    attempts += 1

    if pin == correct_pin:
        print("Access granted")
        break

    remaining = max_attempts - attempts

    if remaining > 0:
        print("Incorrect PIN.")
        print("Attempts remaining:", remaining)
    else:
        print("Account locked.")