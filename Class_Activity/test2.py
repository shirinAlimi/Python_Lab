import pandas as pd
data = {
    "Date": ["2026-4-6", "2025-8-12", "2024-6-10", "2023-6-11"],
    "Sales": [3000, 5000, 4000, 8000]
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
print(df)

import matplotlib.pyplot as plt
df["Sales"].plot()
df["Sales"].plot(kind="bar")
df["Sales"].plot(kind="hist")
plt.show()