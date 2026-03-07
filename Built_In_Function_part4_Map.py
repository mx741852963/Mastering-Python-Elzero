# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function Or Lambda Function
# ----------------------------------------------------------------
# Use Map With Predefined Function
def formatText(text):
    return f"- {text.capitalize().strip()} -"


myText = ["OSama", "AhmAd", "sayed"]
# myFormatedData = map(formatText, myText)
# print(myFormatedData)
for name in list(map(formatText, myText)):
    print(name)
# Use Map With Lambda Function
myText = ["OSama", "AhmAd", "sayed"]
for name in list(map(lambda text: f"- {text.capitalize().strip()} -", myText)):
    print(name)
