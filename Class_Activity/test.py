import pandas as pd
import numpy as np
data = pd.DataFrame({
    "Department": ["CS", "Math", "CS", "Math"],
    "Gender": ["Male", "Male", "Female", "Male"],
    "Marks": [88, 95, 90, 85]
})

pivot = pd.pivot_table(
    data,
    values= "Marks",
    columns= "Gender",
    index= "Department",
    aggfunc= "max"
)

print(pivot)

table = pd.crosstab(data["Department"], data["Gender"])
print(table)