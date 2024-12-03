#!/usr/bin/python3.11
import time
from math import inf

def parse_maps(lines):
    maps = {}
    maptext = []
    title = ""
    for i, line in enumerate(lines):
        if i == 0: continue # seeds
        line = line.strip()
        if line:
            if line[0].isdigit():
                maptext.append(line)
            else:
                title = line
        if not line or i == len(lines) - 1:
            if maptext:
                match title:
                    case "seed-to-soil map:":
                        maps["seed2soil"] = Map(maptext)
                    case "soil-to-fertilizer map:":
                        maps["soil2fert"] = Map(maptext)
                    case "fertilizer-to-water map:":
                        maps["fert2watr"] = Map(maptext)
                    case "water-to-light map:":
                        maps["watr2lght"] = Map(maptext)
                    case "light-to-temperature map:":
                        maps["lght2temp"] = Map(maptext)
                    case "temperature-to-humidity map:":
                        maps["temp2humd"] = Map(maptext)
                    case "humidity-to-location map:":
                        maps["humd2locn"] = Map(maptext)
            maptext = []
            title = ""
            continue
    return maps


class Map:
    def __init__(self, maptext):
        self.m = []
        for line in maptext:
            # 1st val of destination range, 1st val of source range, range len
            dst, src, length = [int(n) for n in line.split(" ")]
            self.m.append((dst, src, length))
        self.nranges = len(self.m)

    def get(self, index):
        for i in range(self.nranges):
            dst, src, length = self.m[i]
            # if in source range, then it has a corresponding val in dest range
            if index >= src and index <= src + length:
                return dst + (index - src)
        return index
    
    def __str__(self):
        out = ""
        for i in range(self.nranges):
            out += str(self.m[i])
        return out


def get_loc(seed):
    seed = int(seed)
    soil = MAPS["seed2soil"].get(seed)
    fert = MAPS["soil2fert"].get(soil)
    watr = MAPS["fert2watr"].get(fert)
    ligt = MAPS["watr2lght"].get(watr)
    temp = MAPS["lght2temp"].get(ligt)
    humd = MAPS["temp2humd"].get(temp)
    loc  = MAPS["humd2locn"].get(humd)
    return loc

with open("input.txt", "r") as f:
    LINES = f.read().split("\n")
MAPS = parse_maps(LINES)

def part1():
    seeds = [int(s) for s in LINES[0].split(": ")[-1].split(" ")]
    ans = inf
    for seed in seeds:
        ans = min(ans, get_loc(seed))
    return ans


def brute_part2():
    seeds = [int(s) for s in LINES[0].split(": ")[-1].split(" ")]
    seeds = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
    ans = inf
    t0 = time.time()
    for i, (mins, maxs) in enumerate(seeds):
        print(f"seed range {i}/{len(seeds)} [et={time.time() - t0 :.2f}s]")
        for s in range(mins, maxs):
            ans = min(ans, get_loc(s))
    return ans


def part2():
    lowest = inf
    seeds = [int(s) for s in LINES[0].split(": ")[-1].split(" ")]
    seeds = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
    maps = []
    for m in MAPS.values():
        pass

    # seed --....--> loc, minimize loc
    # :/
    return lowest


print(part1())
print(brute_part2())