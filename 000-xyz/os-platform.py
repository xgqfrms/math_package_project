#!/usr/bin/env python3
# coding: utf8

__author__ = 'xgqfrms'
__editor__ = 'vscode'
__version__ = '1.0.1'
__copyright__ = """
  Copyright (c) 2012-2050, xgqfrms; mailto:xgqfrms@xgqfrms.xyz
"""

import os
import platform

# print("os =", os)
# os = <module 'os' from '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/os.py'>

# __path = os.path
# print("__path =", __path)
# __path = <module 'posixpath' from '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/posixpath.py'>

path = './os.py'
shell = './multi-line-comments.sh'
cat1 = '/Users/xgqfrms-mm/Documents/github/math_package_project/000-xyz/cat-1.sh'
cat2 = '/Users/xgqfrms-mm/Documents/github/math_package_project/000-xyz/cat-2.sh'


abspath = os.path.abspath(path)
basename = os.path.basename(path)
# commonpath = os.path.commonpath([path, shell, cat1, cat2])
# ValueError: Can't mix absolute and relative paths ❌
# 相对路径与绝对路径不可以混用
# commonpath = os.path.commonpath([path, shell])
# 相对路径，返回空
commonpath = os.path.commonpath([cat1, cat2])
commonprefix = os.path.commonprefix([cat1, cat2])

print("abspath =", abspath)
# abspath = /Users/xgqfrms-mm/Documents/github/math_package_project/000-xyz/os.py
print("basename =", basename)
# basename = os.py
print("commonpath =", commonpath)
# commonpath = /Users/xgqfrms-mm/Documents/github/math_package_project/000-xyz
print("commonprefix =", commonprefix)
# commonprefix = /Users/xgqfrms-mm/Documents/github/math_package_project/000-xyz/cat-

unicode = os.path.supports_unicode_filenames;
# Python Ternary Operator 🐍
print("\nunicode =",  "✅" if unicode else "❌")
# unicode = ✅

# print("\nunicode =", unicode ? "✅" : "❌")
# ❌ SyntaxError: invalid syntax


dirname = os.path.dirname(path)
exists = os.path.exists(path)
lexists = os.path.lexists(path)
expandvars = os.path.expandvars(path)
getatime = os.path.getatime(path)
getmtime = os.path.getmtime(path)
getctime = os.path.getctime(path)

getsize = os.path.getsize(path)
isabs = os.path.isabs(path)
isfile = os.path.isfile(path)
isdir = os.path.isdir(path)

islink = os.path.islink(path)
ismount = os.path.ismount(path)
normpath = os.path.normpath(path)
normcase = os.path.normcase(path)
split = os.path.split(path)
splitdrive = os.path.splitdrive(path)
splitext = os.path.splitext(path)

# join = os.path.isdir(path, *paths)
# realpath = os.path.realpath(path, *, strict=False)
# relpath = os.path.relpath(path, start=os.curdir)¶
# samefile = os.path.samefile(path1, path2)
# sameopenfile = os.path.sameopenfile(fp1, fp2)
# samestat = os.path.samestat(stat1, stat2)






__platform = platform.system()
print("__platform =", __platform)
# __platform = Darwin

MACOS = (__platform == "Darwin")
WINDOWS = (__platform == "Windows")

print("\nMACOS =", MACOS)
# MACOS = True
print("WINDOWS =", WINDOWS)
# WINDOWS = False

# https://github.com/pdm-project/pdm/blob/main/install-pdm.py#L24


# cd ./000-xyz && python3 os.py


"""

https://www.runoob.com/python/os-file-methods.html

https://www.runoob.com/python3/python3-os-file-methods.html


https://docs.python.org/zh-cn/3/library/os.html

https://docs.python.org/zh-cn/3/library/os.path.html#module-os.path

https://docs.python.org/zh-cn/3/library/platform.html

"""
