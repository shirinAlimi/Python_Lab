import pandas as pd
#DataFram form list of lists
data = [
    ["A", 90],
    ["B", 98],
    ["C", 80]
]

df = pd.DataFrame(data, columns=["Name", "Marks"])
print(df)

#DataFram from Dictionary
data1 = {
    "Name": ["X", "Y", "Z"],
    "Marks": [99, 80, 86]
}
s = pd.DataFrame(data1)
print(s)

#DataFram from list of Dictionary
data2 = [
    {"Name": "M", "Marks": 55},
    {"Name": "N", "Marks": 88},
    {"Name": "O", "Marks": 99}
]
t = pd.DataFrame(data2)
print(t)