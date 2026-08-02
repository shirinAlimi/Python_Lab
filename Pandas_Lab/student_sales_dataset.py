import pandas as pd
import numpy as np
students = pd.read_csv("students_dirty_dataset .csv")
print(students.head)

#Cleaning the Student Dataset
#Step1: Create a Copy
students_clean = students.copy()

#Step2: Remove Duplicate Student IDs
students_clean = students_clean.drop_duplicates(
    subset = "StudentID",
    keep= "first"
)
print(students_clean.shape)

#Step3: Clean Names
students_clean["Name"] = students_clean["Name"].fillna("")
students_clean["Name"] = (
    students_clean["Name"].astype(str).str.replace(r"[^A-Z a-z .'-]", "",regex = True)
    .str.strip().str.title()
)
missing_name = students_clean["Name"].eq("")
students_clean.loc[missing_name, "Name"] = ("Unknown_" +
students_clean.loc[missing_name, "StudentID"].astype(str))

#Step4: Standardize Gender
students_clean["Gender"] = (
    students_clean["Gender"].astype("string")
    .str.strip()
    .str.upper()
)
gender_map = {
    "M": "M",
    "MALE": "M",
    "FEMALE": "F",
    "F": "F"
}
students_clean["Gender"] = (
    students_clean["Gender"].map(gender_map)
    .fillna("Unknown")
)

#Step5: Clean Department
students_clean["Department"] = (
    students_clean["Department"].astype("string").str.strip()
    .str.upper()
    .fillna("Unknown")
)
students_clean["Department"] = students_clean["Department"].replace("N/A", "Unknown")

#Step6: Correct Numeric Data Types
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
        errors ="coerce"
)
   
#Step7: Clean Age
valid_age = students_clean["Age"].between(16, 100)

age_median = students_clean.loc[
    valid_age, "Age"
].median()

students_clean.loc[
    ~valid_age | students_clean["Age"].isna(),
    "Age"
] = age_median

students_clean["Age"] = students_clean["Age"].round().astype(int)

#Step8: Clean StudyHours
#Find valid study hours (between 0 and 24)
valid_hours = students_clean["StudyHours"].between(0, 24)
# Calculate the median of only the valid values
hours_median = students_clean.loc[
    valid_hours, "StudyHours"
].median()
# Replace invalid or missing values with the median
students_clean.loc[
    ~valid_hours | students_clean["StudyHours"].isna(),
    "StudyHours"
] = hours_median
# Round the values and convert them to integers
students_clean["StudyHours"] = students_clean[
    "StudyHours"
].round().astype(int)

#Step9: Clean Attendance
valid_attendance = students_clean["Attendance"].between(0, 100)
attendance_median = students_clean.loc[
    valid_attendance, "Attendance"
].median()
students_clean.loc[
    ~valid_attendance | students_clean["Attendance"].isna(),
    "Attendance"
] = attendance_median
students_clean["Attendance"] = students_clean["Attendance"].round().astype(int)

#Step10: Clean Subject Marks
subjects = ["Math", "Physics", "Programming"]
for subject in subjects:
    valid_marks = students_clean[subject].between(0, 100)
    subject_median = students_clean.loc[
        valid_marks, subject
    ].median()
    students_clean.loc[
        ~valid_marks | students_clean[subject].isna(),
        subject
    ] = subject_median
    students_clean[subject] = students_clean[subject].round().astype(int)

#Step11: Compute New Columns
students_clean["Average"] = students_clean[
    ["Math", "Physics", "Programming"]
].mean(axis=1).round(2)
students_clean["Result"] = np.where(
    students_clean["Average"] >= 40,
    "Pass",
    "Fail"
)

#Compute Grade
def assign_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

students_clean["Grade"] = students_clean["Average"].apply(assign_grade)
print(students_clean)
print ( students_clean.isnull().sum())
print("Duplicates: ", students_clean["StudentID"].duplicated().sum())
print ( students_clean["Age"].between(16 , 100).all())
print ( students_clean["Attendance"].between(0 , 100).all())
print ( students_clean["Math"]. between(0 , 100).all())
students_clean.to_csv(
    "students_cleaned_dataset.csv",
    index=False
)


#Sales Dataset
sales = pd.read_csv("sales_dirty_dataset.csv")

#Step1: Create a Copy
sales_clean = sales.copy()

#Step2: Remove Duplicate Order IDs
sales_clean = sales_clean.drop_duplicates(
    subset="OrderID",
    keep="first"
)

print(sales_clean.shape)

#Step3: Clean Month
sales_clean["Month"] = (
    sales_clean["Month"]
    .astype("string")
    .str.strip()
    .str.title()
    .fillna("Unknown")
)

valid_months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

sales_clean.loc[
    ~sales_clean["Month"].isin(valid_months),
    "Month"
] = "Unknown"

#Step4: Clean Region
sales_clean["Region"] = (
    sales_clean["Region"]
    .astype("string")
    .str.strip()
    .str.title()
    .fillna("Unknown")
)

#Step5: Clean Product
sales_clean["Product"] = (
    sales_clean["Product"]
    .astype("string")
    .str.strip()
    .str.title()
    .fillna("Unknown")
)

#Step6: Correct Numeric Data Types
numeric_columns = [
    "Quantity",
    "UnitPrice"
]

for column in numeric_columns:
    sales_clean[column] = pd.to_numeric(
        sales_clean[column],
        errors="coerce"
    )

#Step7: Clean Quantity
valid_quantity = sales_clean["Quantity"].between(1, 100)

quantity_median = sales_clean.loc[
    valid_quantity,
    "Quantity"
].median()

sales_clean.loc[
    ~valid_quantity |
    sales_clean["Quantity"].isna(),
    "Quantity"
] = quantity_median

sales_clean["Quantity"] = (
    sales_clean["Quantity"]
    .round()
    .astype(int)
)

#Step8: Clean UnitPrice
valid_price = sales_clean["UnitPrice"].between(1, 10000)

price_median = sales_clean.loc[
    valid_price,
    "UnitPrice"
].median()

sales_clean.loc[
    ~valid_price |
    sales_clean["UnitPrice"].isna(),
    "UnitPrice"
] = price_median

sales_clean["UnitPrice"] = (
    sales_clean["UnitPrice"]
    .round(2)
)

#Step9: Compute TotalSales
sales_clean["TotalSales"] = (
    sales_clean["Quantity"] *
    sales_clean["UnitPrice"]
).round(2)

print(sales_clean.head())
print(sales_clean.isnull().sum())
print("Duplicates: ", sales_clean["OrderID"].duplicated().sum())
print((sales_clean["Quantity"] > 0).all())
print((sales_clean["UnitPrice"] > 0).all())
sales_clean.to_csv(
    "sales_cleaned_dataset.csv",
    index=False
)


#Saving both cleaned datasets
with pd.ExcelWriter(
    "Python_Lab_Cleaned_Datasets.xlsx",
    engine="openpyxl"
) as writer:

    students.to_excel(
        writer,
        sheet_name="Students_Raw",
        index=False
    )

    students_clean.to_excel(
        writer,
        sheet_name="Students_Clean",
        index=False
    )

    sales.to_excel(
        writer,
        sheet_name="Sales_Raw",
        index=False
    )

    sales_clean.to_excel(
        writer,
        sheet_name="Sales_Clean",
        index=False
    )

print("Excel workbook saved successfully!")