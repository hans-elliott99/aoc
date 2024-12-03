#!/usr/bin/env python3

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 16
# hans elliott

class Valve:
    def __init__(self, flow_rate, connected=[]) -> None:
        self.flow_rate = flow_rate
        self.connected = connected



if __name__=="__main__":
    valves = {}
    all_valves = []

    with open("advent-of-code/inputs/test.txt") as f:

        for line in f:
            connected = []
            flowrate, pipes = line.strip().split(";")
            name = flowrate.strip().split()[1]
            fr = flowrate.strip().split("=")[-1]
            for l in pipes.strip().split(","):
                connected.append(l.split()[-1])

            all_valves.append(name)
            valves[name] = (fr, connected)        
        


