import pandas as pd
import numpy as np
students= pd.read_csv("students_dirty_dataset .csv")
print(students.head(7))
print("Shape: ", students.shape)
#Display Rows Containing Missing Values
students_missing_rows = students[students.isnull().any(axis=1)]
print(students_missing_rows)

print(students.isnull().sum())
dublicat_id = students[
    students.duplicated(subset="StudentID", keep=False)
]
print(dublicat_id )

invalid_age = students[
    (students["Age"] < 16)|
    (students["Age"] > 100)
]
print(invalid_age[["StudentID", "Name", "Age"]])

invalid_attendance = students[
    (students["Attendance"] < 0) |
    (students["Attendance"] > 100)
]
print(invalid_attendance)

import pandas as pd

students_clean = students.copy()

students_clean["Physics"] = pd.to_numeric(
    students_clean["Physics"],
    errors="coerce"
)


valid_age = students_clean ["Age"]. between (16 , 100)

age_median = students_clean . loc [
valid_age , "Age"
]. median ()

students_clean.loc[~valid_age | students_clean ["Age"].isna (), "Age"] = age_median
students_clean["Age"] = students_clean["Age"]. round (). astype (int)



sales = pd.read_csv("sales_dirty_dataset.csv")
print(sales.head(7))
print("Shape: ", sales.shape)

# print(students.columns)
# students.info()
# print("\n")
# #print ( students . describe ( include ="all") )
# print ( students . isnull () .sum () )

# Invalid_hour = [
#     (students["StudyHours"] < 0) |
#     (students["StudyHours"] > 24)
# ]
# print(Invalid_hour)

# # invalid_marks = students[
# #     (students["Math"] < 0) |
# #     (students["Math"] > 100)
# # ]
# # print(invalid_marks)

# # invalid_mark = students[
# #     (students["Programming"] < 0) |
# #     (students["Programming"] > 100)
# # ]
# # print(invalid_mark)

# print(students["Gender"].unique())

