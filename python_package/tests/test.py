
# from math_package_xgqfrms import {add, sub, mul, div}
# import math_package_xgqfrms as Math

# ❌
# NameError: name 'math' is not defined
# from math_package_xgqfrms import *

# ✅
# from math_package_xgqfrms import math

# ❌
# ImportError: cannot import name 'add' from 'math_package_xgqfrms' (/Users/xgqfrms-mm/Library/Python/3.9/lib/python/site-packages/math_package_xgqfrms/__init__.py)
# from math_package_xgqfrms import add, sub, mul, div

# ✅ namespace.module
# from math_package_xgqfrms.math import add, sub, mul, div

# ✅ as
from math_package_xgqfrms import math as Math

n1 = 1
n2 = 2
# sum = math.add(n1, n2)
# sum = add(n1, n2)
sum = Math.add(n1, n2)
print("sum =", sum)
# sum = 3

"""

n1 = 3
n2 = 1
minus = sub(n1, n2)
# minus = Math.sub(n1, n2)
print("minus =", minus)
# minus = 2

n1 = 2
n2 = 3
multi = mul(n1, n2)
# multi = Math.mul(n1, n2)
print("multi =", multi)
# multi = 6

n1 = 6
n2 = 2
divide = div(n1, n2)
# divide = Math.div(n1, n2)
print("divide =", divide)
# div = 3.0


"""

# python3 ./tests/test.py
