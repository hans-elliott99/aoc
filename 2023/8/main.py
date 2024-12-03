#!/usr/bin/python3.11
from math import lcm

# AOC 2023 day 8

with open("input.txt", "r") as f:
    LINES = f.read().split("\n")


def part1():
    lines = LINES.copy()
    leftright = lines.pop(0) #left/right ordering
    lines.pop(0) # blank line

    # BUILD NETWORK
    network = {}
    for line in lines:
        nodeid, elements = line.split(" = ")
        network[nodeid] = elements.replace("(", "").replace(")", "").split(", ")

    # TRAVERSE NETWORK
    nodeid = "AAA"
    lr_ix = 0 # left or right?
    steps = 0
    while True:
        steps += 1
        ix = 0 if leftright[lr_ix] == "L" else 1
        nodeid = network[nodeid][ix]
        if nodeid == "ZZZ":
            break
        lr_ix += 1
        if lr_ix == len(leftright):
            lr_ix = 0
    return steps

def part2():
    lines = LINES.copy()
    leftright = lines.pop(0)
    lines.pop(0) # blank line after left/right ordering

    # BUILD NETWORK
    network = {}
    for line in lines:
        nodeid, elements = line.split(" = ")
        network[nodeid] = elements.replace("(", "").replace(")", "").split(", ")

    # TRAVERSE NETWORK
    startnodes = [nid for nid in network.keys() if nid.endswith("A")]
    stepcounts = []
    for nodeid in startnodes:
        lr_ix = 0
        steps = 0
        while True:
            steps += 1
            ix = 0 if leftright[lr_ix] == "L" else 1
            nodeid = network[nodeid][ix]
            if nodeid.endswith("Z"):
                stepcounts.append(steps)
                break
            lr_ix += 1
            if lr_ix == len(leftright):
                lr_ix = 0

    return lcm(*stepcounts)



print("part 1 solution:", part1())
print("part 2 solution:", part2())