cat <<'EOF' >> brightup.sh
#!/bin/bash
curr=`cat /sys/class/backlight/intel_backlight/actual_brightness`
if [ $curr -lt 4477 ]; then
   curr=$((curr+406));
   echo $curr  > /sys/class/backlight/intel_backlight/brightness;
fi
EOF

# https://stackoverflow.com/questions/22697688/how-to-cat-eof-a-file-containing-code/22698106#22698106

