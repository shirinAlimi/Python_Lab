import pandas as pd
import numpy as np
students = pd.read_excel("Python_Lab_Dirty_Datasets.xlsx")
print(students)

# Create a copy
students_clean = students.copy()

# Remove duplicate Student IDs
students_clean = students_clean.drop_duplicates(
    subset="StudentID",
    keep="first"
)


# Clean Names
students_clean["Name"] = (
    students_clean["Name"]
    .fillna("")
    .astype(str)
    .str.replace(r"[^A-Za-z.' -]", "", regex=True)
    .str.strip()
    .str.title()
)

missing_name = students_clean["Name"].eq("")

students_clean.loc[missing_name, "Name"] = (
    "Unknown_" +
    students_clean.loc[missing_name, "StudentID"].astype(str)
)


# Standardize Gender
students_clean["Gender"] = (
    students_clean["Gender"]
    .astype("string")
    .str.strip()
    .str.upper()
)

gender_map = {
    "M": "M",
    "MALE": "M",
    "F": "F",
    "FEMALE": "F"
}

students_clean["Gender"] = (
    students_clean["Gender"]
    .map(gender_map)
    .fillna("Unknown")
)


# Clean Department
students_clean["Department"] = (
    students_clean["Department"]
    .astype("string")
    .str.strip()
    .str.upper()
    .fillna("Unknown")
)

students_clean["Department"] = (
    students_clean["Department"]
    .replace("<NA>", "Unknown")
)


# Convert Numerical Columns
numeric_columns = [
    "Age",
    "StudyHours",
    "Attendance",
    "Math",
    "Physics",
    "Programming"
]

for column in numeric_columns:
    students_clean[column] = pd.to_numeric(
        students_clean[column],
        errors="coerce"
    )


# Clean Age
valid = students_clean["Age"].between(16, 100)
median = students_clean.loc[valid, "Age"].median()

students_clean.loc[
    ~valid | students_clean["Age"].isna(),
    "Age"
] = median


# Clean Study Hours
valid = students_clean["StudyHours"].between(0, 24)
median = students_clean.loc[valid, "StudyHours"].median()

students_clean.loc[
    ~valid | students_clean["StudyHours"].isna(),
    "StudyHours"
] = median


# Clean Attendance
valid = students_clean["Attendance"].between(0, 100)
median = students_clean.loc[valid, "Attendance"].median()

students_clean.loc[
    ~valid | students_clean["Attendance"].isna(),
    "Attendance"
] = median

# Clean Marks
subjects = [
    "Math",
    "Physics",
    "Programming"
]

for subject in subjects:
    valid = students_clean[subject].between(0, 100)

    median = students_clean.loc[
        valid,
        subject
    ].median()

    students_clean.loc[
        ~valid | students_clean[subject].isna(),
        subject
    ] = median

# Derived Columns
students_clean["Average"] = (
    students_clean[subjects]
    .mean(axis=1)
    .round(2)
)

students_clean["Result"] = np.where(
    students_clean["Average"] >= 40,
    "Pass",
    "Fail"
)


# Grade Function
def grade(value):
    if value >= 80:
        return "A"
    if value >= 70:
        return "B"
    if value >= 60:
        return "C"
    if value >= 50:
        return "D"
    return "F"

students_clean["Grade"] = (
    students_clean["Average"]
    .apply(grade)
)


# Save Cleaned Dataset
students_clean.to_csv(
    "students_cleaned_dataset.csv",
    index=False
)

print(students_clean)