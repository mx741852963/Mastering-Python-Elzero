# -------------------------------
# -- Built In Functions => Filter --
# -------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function Or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ----------------------------------------------------------------
# Example 1
def checkNumber(num):
    if num > 10:
        return num


mynum = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
myResult = filter(checkNumber, mynum)
for num in myResult:
    print(num)
# Example 2
for number in filter(lambda number: number > 10, list(range(0, 20))): print(number)

# Example 3
def checkName(name):
    return name.startswith('a')


myText = ['ahmad', 'ali', 'osama']
myResult2 = filter(checkName, myText)
for name in myResult2:
    print(name)
# Example 4
for name in filter(lambda name: name.startswith('a'), ['ahmad', 'ali', 'osama']):
    print(name)
# Example 5
myNames = ['ahmad', 'ali', 'osama']
myResultNames = filter(lambda name: name.startswith('a'), myNames)
for name in myResultNames:
    print(name)
