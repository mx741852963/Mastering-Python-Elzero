# =================================================================
#                 FILTERING STRATEGIES FOR ML
# =================================================================
# 1. Boolean Masking: Creating a series of True/False values to 'mask' rows.
# 2. .isin(): Powerful for filtering categorical data (e.g., specific countries).
# 3. .str.contains(): Essential for searching sub-strings in text columns.
# 4. Handling NaNs: Always use 'na=False' in string methods to avoid crashes.
# =================================================================
# LOGICAL NEGATION & MISSING DATA (na)
# =================================================================
# 1. The Tilde Operator (~):
# - This is the standard 'Bitwise NOT' in Pandas.
# - Use it to invert your filter (True becomes False and vice versa).
# - Example: df.loc[~mask] means "Give me everything EXCEPT the mask".

# 2. The Minus Sign (-):
# - This is an 'Arithmetic Unary Minus'.
# - While it may work in some cases (True becomes -1, False stays 0),
#   it is NOT recommended for logical filtering. Always use (~).

# 3. The 'na' Parameter:
# - 'na' is the predefined parameter in pandas string methods (like .contains).
# - It tells Pandas how to treat NaN (Not a Number) values.
# - Setting na=False ensures the filter returns False for empty cells instead of an Error.
# =================================================================
# Filtering The Data
import pandas as pd

df = pd.read_csv(r"data\survey_results_public.csv")
df_schema = pd.read_csv(r"data\survey_results_schema.csv", index_col="Column")
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
high_salary = ((df['ConvertedComp'] > 70000) & (df['LanguageWorkedWith'] == 'Python'))
print(df.loc[high_salary, ['ConvertedComp', 'LanguageWorkedWith']])
Countries = ["United Kingdom", "United States", "Canada", "Spain"]
high_salary = ((df['ConvertedComp'] > 70000) & (df['LanguageWorkedWith'] == 'Python') & df['Country'].isin(Countries))
print(df.loc[high_salary, ['ConvertedComp', 'LanguageWorkedWith', 'Country']])
mask = df['LanguageWorkedWith'].str.contains('Python', na=False)
print(df.loc[~mask, 'Country'])
print(df.loc[-mask, 'Country'])
print(df.loc[mask, 'Country'])
