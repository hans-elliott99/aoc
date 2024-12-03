#!/usr/bin/python3.11

NUMBER = ["zero", "0", "one", "1", "two", "2", "three", "3", "four", "4",
          "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9"]

def tointstr(numstr):
    if numstr.isdigit():
        return numstr
    return str(NUMBER.index(numstr) // 2)

def mapnum(string):
    # brute force
    nums = []
    nchar = len(string)
    for i in range(0, nchar):
        for j in range(1, nchar+1):
            s = string[i:j]
            if s in NUMBER:
                nums.append(tointstr(s))
    # adjust specific cases
    if len(nums) == 0:
        nums = ["0"]
    elif len(nums) == 1:
        nums = nums + nums
    elif len(nums) > 2:
        nums = nums[0] + nums[-1]
    return int("".join(nums))


with open("day1.txt", "r") as f:
    lines = f.readlines()

calibration_values = []
for line in lines:
    line = line.strip()
    calibration_values.append(mapnum(line))


print(f"{sum(calibration_values) = }")