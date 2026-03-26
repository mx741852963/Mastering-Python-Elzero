# =================================================================
#                      WHY INDEXING MATTERS?
# =================================================================
# 1. Fast Lookup: Searching for a 'Respondent' by ID is O(1) time complexity
#    when it's an Index, much faster than a standard search.
# 2. Schema Mapping: Making 'Column' the index in schema allows us to
#    instantly translate technical column names to human questions.
# 3. Data Alignment: Sorting by Index ensures consistent behavior
#    when merging or joining with other datasets in ML.
# =================================================================
import pandas as pd

df = pd.read_csv(r"data\survey_results_public.csv", index_col="Respondent")
# index_col="Respondent" make Respondent The main index
df_schema = pd.read_csv(r"data\survey_results_schema.csv", index_col="Column")
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
# print(df.loc[1])

# print(df.set_index('Hobbyist'))
# df.set_index('Gender', inplace=True)
# print(df)
# print(df.index)
# ndex(['Man', 'Man', 'Man', 'Man'.....................
# df.reset_index(inplace=True)
# print(df.index)  # RangeIndex(start=0, stop=88883, step=1)
# index_col="Column" make "Column" The main index in schema to
# help us find a question(not understand) in main cv
# like  MgrIdiot in main cv did not match any things to some people so by make index_col="Column"
# in schema can access the Question without search one by one in schema
# print(df_schema.loc["MgrIdiot", 'QuestionText'])
# How confident are you that your manager knows what they’re doing?
print(df_schema.sort_index())  # alphabetic
# print(df_schema.sort_index(ascending=False))
