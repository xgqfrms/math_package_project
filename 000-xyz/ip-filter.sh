#!/usr/bin/env bash

# 写死文件的绝对路径 👎
# input="/absolute/path/to/file.txt"

# 动态读取 参数 ✅
input=$1

rgexp='192\.168\.(1?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([2-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])\b'

# while IFS= read -r line
while read -r line
do
  echo "$line"
  # match regex ???
  # rgexp.test($line)
  # echo "$line" | sed -e 's/rgexp//' -n
  # echo "$line" | sed -e 's/192\.168/✅/' -n
  # echo "$line" | sed -e 's/192\.168/✅/'
  # printf "$line" | sed -e 's/192\.168/✅/' > ./ip.md
  # printf "$line" | sed -e 's/192\.168/✅/' > ./ip.md
  # if echo "$line" | sed -e 's/192\.168/✅/' -n
  if echo "$line" | sed -e 's/192\.168/✅/'
  then
    echo "✅"
  else
    echo "❌"
  fi
done < "$input"


<<EOF
$ echo "this is abc" | sed -e 's/abc/xyz/'
this is xyz
# 不输出
$ echo "this is abc" | sed -e 's/abc/xyz/' -n

EOF


# $ ./ip-filter.sh ./ifconfig.txt

# https://www.cnblogs.com/xgqfrms/p/17362135.html
