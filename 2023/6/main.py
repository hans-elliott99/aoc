#!/usr/bin/python3.11


with open("input.txt", "r") as f:
    times, dists = f.read().split("\n")


def part1():
    time = times.split(":")[-1].strip().split()
    dist = dists.split(":")[-1].strip().split()

    tot = 1
    for i in range(len(time)):
        t, d = int(time[i]), int(dist[i])
        wincnt = 0
        for j in range(1, t):
            race = t - j      # ms spent racing
            travel = race * j # dist traveled
            if travel > d:
                wincnt += 1
        tot *= wincnt
    return tot


def part2():
    time = int(times.split(":")[-1].replace(" ", ""))
    dist = int(dists.split(":")[-1].replace(" ", ""))

    wincnt = 0
    for j in range(1, time):
        race = time - j   # ms spent racing
        travel = race * j # dist traveled
        if travel > dist:
            wincnt += 1
    return wincnt


print("part 1 solution:", part1())
print("part 2 solution:", part2())