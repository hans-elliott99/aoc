#!/usr/bin/python3.11
import re

with open("day1.txt", "r") as f:
    lines = f.readlines()


calibration_values = []
for line in lines:
    line = line.strip()
    num = re.sub("[^0-9]", "", line)
    if len(num) == 0:
        num = 0
    elif len(num) == 1:
        num = num + num
    elif len(num) > 2:
        num = num[0] + num[-1]
    calibration_values.append(int(num))

print(f"{sum(calibration_values) = }")


    