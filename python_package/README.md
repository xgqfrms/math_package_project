# xgqfrms_package_math

> A math package of python 3. 🐍

This package includes math methods: `add`ition, `sub`traction, `mul`tiplication and `div`ision.

## PyPI

https://pypi.org/user/xgqfrms/

https://pypi.org/project/math_package_xgqfrms/

<!-- https://pypi.org/project/gpio/ -->
<!-- https://pypi.org/project/math-package/ -->

## GitHub

[math_package_project](https://github.com/xgqfrms/math_package_project)


## Project tree

```sh
# math_package_project
$ tree
.
├── LICENSE
├── README.md
├── pyproject.toml
├── src
│   └── math_package_xgqfrms
│       ├── __init__.py
│       └── math.py
└── tests
    └── demo.py
```


## Examples

1. add

```py
import math_package_xgqfrms as Math

n1 = 1
n2 = 2
sum = Math.add(n1, n2)
print("sum =", sum)
# sum = 3

```

2. sub

```py
import math_package_xgqfrms as Math

n1 = 3
n2 = 1
minus = Math.sub(n1, n2)
print("minus =", minus)
# minus = 2

```

1. mul

```py
import math_package_xgqfrms as Math

n1 = 2
n2 = 3
multi = Math.mul(n1, n2)
print("multi =", multi)
# multi = 6

```

1. div

```py
import math_package_xgqfrms as Math

n1 = 6
n2 = 2
divide = Math.div(n1, n2)
print("divide =", divide)
# div = 3.0

```
