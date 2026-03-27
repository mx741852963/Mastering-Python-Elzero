# =================================================================
#          ENGINEERING TIPS FOR DATA TRANSFORMATION
# =================================================================

# 1. Performance: Use .at[] instead of .loc[] when updating a SINGLE cell.
#    It is optimized for speed and uses less memory.

# 2. Safety (map vs replace):
#    - .map() will turn unmentioned values into NaN (Dangerous for real data!).
#    - .replace() keeps unmentioned values as they are (Much safer).

# 3. Vectorization: Whenever possible, use built-in pandas string methods
#    like df['col'].str.lower() instead of .apply(lambda x: x.lower()).
#    Pandas string methods are "Vectorized" and much faster on large datasets.

# 4. Chain Assignment Warning: Never use df[mask]['column'] = value.
#    Always use df.loc[mask, 'column'] = value to ensure the change
#    happens in the original memory, not a temporary copy.
# =================================================================
# Updating rows and columns
import pandas as pd

people = {
    "First name": ["John", "mark", "alexa"],
    "Last name": ["Doe", "Los", "kol"],
    "Age": [25, 30, 42],
    "Gender": ["Male", "Male", "Female"],
}
df = pd.DataFrame(people)
# print(df.columns) # View The Columns
# change The Columns Indexing And Name Just The index of column not the content
df_1 = df.columns = ['Last name', 'First name', 'Age', 'Gender']
# Here you can access column name and do everything like make the name lower
df.columns = [x.lower() for x in df.columns]
df.columns = df.columns.str.replace(' ', "_")  # Here replace the " " by "_"
df.rename(columns={'first_name': "first"}, inplace=True)  # Here rename but when inplace not true
#  the change is  temporary , more safety to data
# Here you can access to data but in series not dataframe
# you can change name or age ..........
df.loc[2] = ["ahmad", "ahmad", 20, "Male"]
df.loc[0] = ["loay", "aljmal", 12, "Female"]
df.loc[2, ['last_name', 'first']] = ["Akram", "Mark"]
df.loc[2, ['last_name', 'age']] = ["Akram", 60]
df.loc[2, ['last_name']] = "sad"
# here at faster in memory I guess
df.at[2, 'last_name'] = "Maeda"
# ------------------------------
# Here you Defined filter
mask = df["gender"] == "Female"
# print(df[mask])
# loay  aljmal   12  Female
print(df[mask]['first'])  # Here if series accept the filler return 'first'
# df[mask]['first'] = 'smith' error you can not replace value like this loc can do this
df.loc[mask, 'first'] = 'smith'  # here any series accept mask : do the changes
df.loc[mask, 'gender'] = 'Male'
df["gender"].str.upper()  # all data in gender column became uppercase
df["gender"] = df["gender"].str.lower()  # another way
# ------------- apply method -----------------------
# apply() can access series
df['first'].apply(len)  # here return length of data in "first" column
df['last_name'].apply(len)  # same thing


# apply() accept function
def update_1(gender):
    return gender.upper()


df['gender'].apply(update_1)  # here every item in "gender" columns became uppercase


def update_2(gender):
    return gender == 'male'


df['gender'].apply(update_2)  # here every item became male


def update_3(gender):
    gender = 'NAN'
    return gender


df['gender'].apply(update_3)  # # here every item became NAN
df["gender"] = df['gender'].apply(update_1)  # another way
# ok you can do these things with lambda
df["gender"] = df['gender'].apply(lambda x: "nan" if x == "Female" else "MALE")
df["age"] = df['age'].apply(lambda x: "+18" if x >= 18 else "Go To Sleep")
df["last_name"] = df['last_name'].apply(lambda x: "Mark" if x else x == "nan")
df['last_name'].apply(len)  # one rows
df.apply(len)  # every column have three values
df.apply(len, axis='columns')  # every raw have four values
print(df.apply(pd.Series.min))  # return the min  Series : str => Alphabetical : num > numerical
print(df.apply(pd.Series.max))  #
df.apply(lambda x: x.min())  # Same because apply make change to Series
df.apply(lambda x: x.max())
# ---------- map method ---------------
# can access dataframe
print(df.map(str.title))  # make all dataframe title but be Carefully if dataframe contain number return error
df['last_name'].map({"Mark": 'Ali'})  # here temporary
df['last_name'] = df['last_name'].replace({"Mark": 'Ali'})  # here permanently
# -------------------------------------- REAl DATA -------------------------------------------------
df = pd.read_csv(r"data\survey_results_public.csv")
df_schema = pd.read_csv(r"data\survey_results_schema.csv")
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
df.rename(columns={"ConvertedComp": "SalaryUSD"}, inplace=True)
# print(df["SalaryUSD"])
# print(df["Hobbyist"].map({"Yes": True, "No": False})) # here temporary
# df["Hobbyist"] = df["Hobbyist"].map({"Yes": True, "No": False})  # here permanently
print(df["Hobbyist"])
