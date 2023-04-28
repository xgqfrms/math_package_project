#!/usr/bin/env bash


# TODO: python3 & pip3 install checker
# if not installed then
#   # install promoto
#   echo "❌"
# else
#   echo "✅"
# fi

rm -rf ./python_package/dist/*.*

# ⚠️ 必须要先进入 python project package 的目录，才能执行构建打包和上传文件
cd ./python_package/
# && 串行
./build.sh && ./upload.sh


<<EOF
"""

# && 串行
./python_package/build.sh && ./python_package/upload.sh

ERROR Source /Users/xgqfrms-mm/Documents/github/math_package_project does not appear to be a Python project: no pyproject.toml or setup.py
build ✅
ERROR    InvalidDistribution: Cannot find file (or expand pattern): 'dist/*'
upload ✅

"""
EOF
