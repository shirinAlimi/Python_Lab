import pandas as pd
import numpy as np

df = pd.read_csv("Class_Activity/students_dirty_dataset .csv")
# print ( df . iloc [0:3 , 0:2])
# print(df.isnull())
# print(df.isnull().sum())
clean = df.dropna()
print(clean)
# df["Mark"] = df[["Math", "Programming"]].sum(axis=1)
# print(df)
# df["Physics"] = df["Physics"].replace("Absent", 0)
# df["Physics"] = pd.to_numeric(df["Physics"], errors="coerce")
# print(df)
# df["Average"] = df[["Math","Programming", "Physics"]].mean(axis=1)
# print(df)
# df["Marks"] = df["Average"].apply(lambda x:"A" if x>= 80 else  ("B" if x>= 70 else "C"))
# print(df)
# import matplotlib.pyplot as plt
# df.plot(kind="scatter", x = "StudyHours", y = "Math")
# plt.show()
# print(df.head(3))
# print(df.tail(3))
# print(df.shape)
# print(df.columns)
# print(df.index)
# print(df.info())
# print(df.describe())
# print(df["Name"])
# print(df[["Name", "StudentID"]])
# print(df.loc[0])
# print(df.loc[0:2, ["Name", "StudentID"]])
# print("\n")
# print(df.iloc[0])

# highe_number = df[df["StudyHours"]>15]
# print(highe_number[["Name", "StudyHours"]])

# filtered = df[(df["Math"]> 70) & (df["Gender"] == "F")]
# print(filtered[["Name", "Math", "Gender"]])
# sorted_df = df.sort_values("StudyHours")
# print(sorted_df[["Name", "StudyHours"]])
# sorted_df1 = df.sort_values("StudyHours", ascending= False)
# print(sorted_df1[["Name", "StudyHours"]])
# sort = df.sort_values(["Math", "Programming"], ascending= False)
# print(sort[["Name", "Math", "Programming"]])
# df["Pass"] = df["Math"] >= 70
# print(df)
# df["Bonous"] = df["Math"] + 5
# print(df)
# df = df.drop("Bonous", axis= 1)
# print(df)
# df = df.rename(columns={"Math":"M"})
# print(df)
# df = df.rename(columns={"Physics": "Ph"})
# print(df)
# df.to_csv("MyOutput.csv", index= False)

# v= pd.read_excel("Class_Activity/students_dirty_dataset.xlsx")
# print(v.head(3))
# v.to_excel("MyOutput2.xlsx", index= False)

