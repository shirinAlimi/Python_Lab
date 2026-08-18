text = input("Enter text: ")

frequency = {}

for character in text.lower():
    if character.isalpha():
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

for character in sorted(frequency):
    print(character + ":", frequency[character])