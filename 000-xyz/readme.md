# Python Project Package

```sh
# .zshrc
$ python --version
# Python 3.9.6

$ python3 --version
# Python 3.9.6

# macOS
$ python3 -m pip install --upgrade pip

# pip ❌
$ pip --version
# zsh: command not found: pip

# pip3 ✅
$ pip3 --version
# pip 23.0.1 from /Users/xgqfrms-mm/Library/Python/3.9/lib/python/site-packages/pip (python 3.9)


```

```sh
$ cd python-project-package/xgqfrms_package_math/src
$ chmod +x ./main.py
$ ./main.py
# xgqfrms's first Python 3 Project Package ✅
```


https://packaging.python.org/en/latest/tutorials/packaging-projects/


## PyPI

> Python Package Index


https://pypi.org/search/


https://pypi.org/project/math_package_xgqfrms/

https://pypi.org/project/gpio/

https://github.com/pypa/packaging-problems


## tree

```sh

packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── example_package_YOUR_USERNAME_HERE/
│       ├── __init__.py
│       └── example.py
└── tests/

```

https://pypi.org/user/xgqfrms/


## `modules` and `import packages`

https://docs.python.org/3/tutorial/modules.html#packages

https://packaging.python.org/en/latest/glossary/#term-Import-Package

https://packaging.python.org/en/latest/glossary/#term-Module

https://packaging.python.org/en/latest/glossary/#term-Distribution-Package

https://packaging.python.org/en/latest/key_projects/#hatch

https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata



https://pypi.org/classifiers/

https://packaging.python.org/en/latest/glossary/#term-Source-Distribution-or-sdist



## TOML

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "math_package_xgqfrms"
version = "0.0.1"
authors = [
  { name="xgqfrms", email="xgqfrms@xgqfrms.xyz" },
]
description = "A math package of python 3. 🐍"
readme = "README.md"
requires-python = ">=3.7"
classifiers = [
  "Intended Audience :: Developers",
  "Programming Language :: Python :: 3",
  "Topic :: Software Development :: Libraries :: Python Modules",
  "Operating System :: OS Independent",
  "License :: OSI Approved :: MIT License",
]
keywords = [
  "math",
  "package",
  "python",
  "xgqfrms",
  "linux",
]
license = "MIT"
# license_files = "LICENSE"
# Additional properties are not allowed ('license_files' was unexpected)Even Better TOML ❌


[project.urls]
"Homepage" = "https://github.com/xgqfrms/math_package_project"
"Bug Tracker" = "https://github.com/xgqfrms/math_package_project/issues"
```


https://github.com/pypa/sampleproject/blob/main/pyproject.toml


## test

https://test.pypi.org/

```sh
# --repository testpypi
$ python3 -m twine upload --repository testpypi dist/*

$ python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps math_package_project

# ???
$ pip3 install -i https://test.pypi.org/simple/ math-package-xgqfrms==0.0.1

```


https://test.pypi.org/project/math-package-xgqfrms/0.0.1/

# prod

https://pypi.org/

```sh
$ python3 -m twine upload dist/*

$ python3 -m pip install math_package_project

$ pip3 install math_package_project==0.0.1

```

https://pypi.org/project/math-package-xgqfrms/0.0.1/

## refs

https://packaging.python.org/en/latest/tutorials/packaging-projects/

https://www.cnblogs.com/xgqfrms/p/17271108.html

