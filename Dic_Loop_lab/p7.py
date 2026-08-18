student = {
    "name": "Aura",
    "identification number": "AUW123",
    "program": "Computer Science",
    "year of study": 3
}

print("Original dictionary:")
print(student)

new_year = input("Enter new year of study: ")
student["year of study"] = new_year

student["email"] = input("Enter email: ")

print("\nStudent information:")

for key, value in student.items():
    print(key, ":", value)

if "phone" in student:
    print("Phone key exists.")
else:
    print("Phone key does not exist.")