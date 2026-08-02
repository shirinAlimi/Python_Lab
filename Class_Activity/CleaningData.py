import pandas as pd
import numpy as np

data = {
    "Name": ["Shirin", "Ali", "Ena", "Zahra", "Sam"],
    "Marks": [99, 100, np.nan, 88, 78],
    "Major": ["CS", "Math", "Econ", np.nan, "English"]
}
df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())
clean = df.dropna()
print(clean)

# df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
# print(df)

df["Major"] = df["Major"].fillna("CS")
print(df)

df= df.fillna(50)
print("\n", df)

# print(df["Marks"].mean())
# print(df["Marks"].median())
print(df["Marks"].mode())