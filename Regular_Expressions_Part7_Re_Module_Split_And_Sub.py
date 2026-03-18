# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# ----------------------------------------------------
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Split On Each Match
# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
# ---------------------------------------------------------------------
import re

string_one = "I Love Python A_Z"
search_one = re.split(r"\s", string_one, 1)
print(search_one)
print("'" * 50)
string_two = "How-To_Write_A_Very-Good-Article"
search_two = re.split(r"[-_]", string_two)
print(search_two)
print("'" * 50)
# Get Word From URl
for counter, item in enumerate(search_two, 1):
    if len(item) == 1:
        continue
    print(f"{counter}. {item.lower()}")
print("'" * 50)
print(re.sub(r"[-_]", " ", string_two, 5))
