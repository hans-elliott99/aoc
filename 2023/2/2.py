#!/usr/bin/python3.11
from math import prod

with open("input.txt", "r") as f:
    lines = f.readlines()

total_cubepower = 0
for line in lines:
    line = line.strip()
    game, sets = line.split(":")
    game = int(game.split(" ")[-1])
    sets = sets.strip().split(";")

    cubedict = {"red":1,"blue":1,"green":1}
    for i, draw in enumerate(sets):
        fail = False
        cubes = draw.split(",")
        for cube in cubes:
            n, color = cube.strip().split(" ")
            n = int(n.strip())
            color = color.strip()
            cubedict[color] = max(cubedict[color], n)

    total_cubepower += prod(cubedict.values()) 

    
print(f"{total_cubepower = }")