# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Modules Is A File Contain A Set Of Functions
# [2] You Can Import Modules In Your App To Hellp You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# ---------------------------------
# Import Main Module
# import random
# print(random)
# print(f"Print Random Float Number: {random.random()}")


# Show All Function Inside Module
# import random
# print(dir(random))

# Import One Or Two Functions From Modules
from random import randint, random

print(f"Print Random Integer {randint(1, 10)}")
print(f"Print Random Float {random()}")
