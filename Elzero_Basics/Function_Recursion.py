# ------------------------
# -- Function Recursion --
# ------------------------
# ----------------------------------------------------------------------
# -- To Understand Recursion , You Need First To Understand Recursion --
# ----------------------------------------------------------------------
# Test Word [WWWoooorrrldd] print(x[1:])
# x="WWWoooorrrldd"
def clean_word(word):
    if len(word) == 1:
        return word
    print(f"Print Start Function {word}")
    if word[0] == word[1]:
        print(f"Print Before Condition {word}")
        return clean_word(word[1:])
    print(f"Print Before Return  {word}")
    return word[0] + clean_word(word[1:])


print(clean_word("WWWoooorrrldd"))
