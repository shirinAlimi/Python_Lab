import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))

    if guess < 1 or guess > 100:
        print("Invalid guess. Enter a number between 1 and 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print("Correct!")
        print("Total attempts:", attempts)
        break