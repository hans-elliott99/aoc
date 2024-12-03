#!/usr/bin/env python3

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 7: No Space Left On Device
# hans elliott

directories = {}

def change_current_dir(line:str, cwd:list[str]) -> list[str]:
    """Update 'cwd' based on the `cd` command"""
    d = line.split(' ')[-1]

    if d == '..':
        cwd = cwd[:-1] ##go back one directory
    elif d == '/':
        cwd = ['/']    ##go back to home
    else:
        cwd.append(d)  ##go forward one directory
    
    cwd_str = '/'.join(cwd)[1:] if len(cwd) > 1 else '/'
    if cwd_str not in directories.keys():
        directories[cwd_str] = 0
    return cwd

def parse_ls_files(line, cwd):
    """Parse files listed by `ls` and add their sizes to all parent dirs"""
    size, f = line.split()
    directories['/'] += float(size)

    path = '/'
    for d in cwd[1:]:
        path += d
        directories[path] += float(size)
        path += '/'    

if __name__=="__main__":

    # First parse commands to get the size of all files within each directory
    with open("advent-of-code/inputs/day7.txt") as f:

        cwd = ["/"] ##current working directory

        for line in f:
            line = line.strip()
            if (line[0] == '$') & (line.split()[1]=='cd'):
                cwd = change_current_dir(line, cwd)

            elif line.split()[0].isdigit():
                parse_ls_files(line, cwd)        


    # Part 1: total size of directories that contain files of size <= 100,000
    part1 = sum( [v for v in directories.values() if v <= 100_000] )

    # Part 2: Size of smallest directory which, if deleted, provides enough
    #          space to incorporate the needed free space           
    total_space, need_free = 70_000_000, 30_000_000
    total_used = directories["/"]
    min_freeup = need_free - (total_space-total_used)

    part2 = min([v for v in directories.values() if v > min_freeup])

    print(f"Part 1 total size: {part1 :.0f}")
    print(f"Part 2 total size: {part2 :.0f}")
