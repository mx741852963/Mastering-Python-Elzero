# __ Pandas Intro __
# =================================================================
# 🛠️ PANDAS ARCHITECTURE & THEORY REFERENCE
# =================================================================

# 1. Definition:
# Pandas (Derived from "Panel Data") is a high-performance open-source
# library for data manipulation and analysis in Python.
# It is built on top of NumPy, which makes it extremely fast.

# 2. Why Pandas for Machine Learning (ML)?
# - Data Cleaning: Handling missing values (NaN), outliers, and noise.
# - Data Alignment: Labeling data with Index and Column names.
# - Heterogeneous Data: Can store different data types (int, float, string)
#   together in one table (DataFrame), unlike NumPy which prefers one type.

# 3. Core Data Structures:
# - Series: A 1D labeled array (like a single column in Excel).
# - DataFrame: A 2D labeled data structure (the whole table/grid).

# 4. Key Differences (Attributes vs Methods):
# - Attributes (.shape, .columns, .index): Fixed properties. (No parentheses)
# - Methods (.head(), .info(), .read_csv()): Actions/Functions. (Use parentheses)

# 5. Metadata (The Schema):
# The 'survey_results_schema.csv' acts as the Data Dictionary or Metadata.
# It explains the meaning of each column in the main dataset.

# =================================================================
import pandas as pd

# df = pd.read_csv(r"data\survey_results_public.csv")
# head() => 1 2 .............
# [5 rows x 85 columns]
# print(df.head())
# [10 rows x 85 columns]
# print(df.head(10))

# tail() => 8000 7999 ................
# [5 rows x 85 columns]
# print(df.tail())
# [10 rows x 85 columns]
# print(df.tail(10))

# shape => return (rows,columns)
# print(df.shape) # =>(88883, 85)

# info() => data type
# df.info()
# dtypes: float64(5), int64(1), str(79)
# memory usage: 57.6 MB

# set_option()
# pd.set_option('display.max_columns', 3)
# pd.set_option('display.max_rows', 5)
# print(df)


# df_schema = pd.read_csv(r"data\survey_results_schema.csv")
# pd.set_option('display.max_rows', 85)
# print(df_schema)
