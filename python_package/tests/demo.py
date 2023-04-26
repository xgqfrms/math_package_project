
# import ./src/math_package_xgqfrms/math.py as Math

"""
Relative imports cannot be used with "import .a" form; use "from . import a" instead Pylance
Expected module name Pylance

Statements must be separated by newlines or semicolons Pylance
Expected expression Pylance

"""

# ✅
from .src.math_package_xgqfrms.math.py import add
# from .src.math_package_xgqfrms.math.py import sub
# from .src.math_package_xgqfrms.math.py import mul
# from .src.math_package_xgqfrms.math.py import div

# ❌
# ImportError: attempted relative import with no known parent package

# ❌
# from .src.math_package_xgqfrms.math.py import add, sub, mul, div

# ❌
# from .src.math_package_xgqfrms.math.py import * as Math
# ❌
# from ./src/math_package_xgqfrms/math.py import add
# from ./src/math_package_xgqfrms/math.py import add, sub, mul, div

# import math_package_xgqfrms as Math

n1 = 1
n2 = 2
sum = add(n1, n2)
# sum = Math.add(n1, n2)
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

# python3 ./tests/demo.py
