import pandas as pd
import numpy as np

sales = pd.read_csv("sales_dirty_dataset.csv")

# Step 1: Create a Copy
sales_clean = sales.copy()

# Step 2: Remove Duplicate Order IDs
sales_clean = sales_clean.drop_duplicates(
    subset="OrderID",
    keep="first"
)

print(sales_clean.shape)

# Step 3: Clean Month
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

# Step 4: Clean Region
sales_clean["Region"] = (
    sales_clean["Region"]
    .astype("string")
    .str.strip()
    .str.title()
    .fillna("Unknown")
)

# Step 5: Clean Product
sales_clean["Product"] = (
    sales_clean["Product"]
    .astype("string")
    .str.strip()
    .str.title()
    .fillna("Unknown")
)

# Step 6: Correct Numeric Data Types
numeric_columns = [
    "Quantity",
    "UnitPrice"
]

for column in numeric_columns:
    sales_clean[column] = pd.to_numeric(
        sales_clean[column],
        errors="coerce"
    )

# Step 7: Clean Quantity
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

# Step 8: Clean UnitPrice
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

# Step 9: Compute TotalSales
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