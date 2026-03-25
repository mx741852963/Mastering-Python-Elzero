# ----------------------------------
# -- Built In Functions => Reduce --
# ----------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On First Element And Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Result And Fourth Element And So On
# [5] Till One Element Is Left And This Is The Result Of The Reduce
# [6] The Function Can Be Pre-Defined Function Or Lambda Function
# ----------------------------------------------------------------
from functools import reduce


def sumAll(num1, num2):
    return num1 + num2


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = reduce(sumAll, numbers)
print(result)

# (((1+2)+3))+......)
result2 = reduce(lambda num1, num2: num1 + num2, numbers)
print(result2)
