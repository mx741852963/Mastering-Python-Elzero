# =================================================================
#        QUICK REFERENCE: PANDAS DATA TYPES & SELECTION
# =================================================================

# 1. DATA TYPES (Series vs DataFrame):
# - Series: A 1D array (Single Column). It's the building block.
# - DataFrame: A 2D table (Rows & Columns). A collection of Series.

# 2. SELECTION (iloc vs loc):
# - iloc (Integer-location): Access by 'Index Position' (Numbers only: 0, 1, 2).
# - loc (Label-location): Access by 'Index Label' (Names/Strings: 'Age', 'Gender').

# Pro Tip: Slicing with 'loc' INCLUDES the last element,
# while 'iloc' (and standard Python) EXCLUDES it.
# =================================================================
# Dict to Csv With pandas

import pandas as pd

people = {
    "Firstname": ["John", "mark", "alexa"],
    "Lastname": ["Doe", "Los", "kol"],
    "Age": [25, 30, 42],
    "Gender": ["Male", "Male", "Female"],
}
# print(people["Age"])
df = pd.DataFrame(people)
# print(df)
print(df['Age'])
print(df['Gender'])
print(df['Lastname'])
print(type(df["Firstname"]))  # =>  <class 'pandas.Series'>
print(df.Age)  # == df['Age'] but  not recommend
print(df[["Age", "Firstname"]])  # multi Columns
print(type(df[["Age", "Firstname"]]))  # <class 'pandas.DataFrame'>
print(df.columns)  # All Columns Index(['Firstname', 'Lastname', 'Age', 'Gender'], dtype='str')
print("_" * 50)
# loc and iloc function
print(df.iloc[0])  # one row all columns

print(df.iloc[[0, 1]])  # two row all columns

print(df.iloc[[0, 1], [0]])  # two row one column

print(df.iloc[[0, 1, 2], [0]])  # three row one column

print(df.iloc[[1], [0, 1, 2]])  # one row three column
print("_" * 50)
print(df.loc[0])
print(df.loc[[0, 1]])
print(df.loc[[0, 1], "Gender"])
print(df.loc[[0, 1], ["Gender", "Lastname"]])
print("_" * 50)
# You Can Slice Dataframe with iloc
print(df.iloc[0:2, 0:1])
