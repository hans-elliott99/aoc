#!/usr/bin/env python3

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 15: Beacon Exclusion Zone (part 1) 
# hans elliott
import string
import sys


def manhattan_distance(p1:tuple, p2:tuple):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def sensor_beacon_dist(idx, sensors:dict):
    """Distance between sensor and its closest beacon.
    """
    sens = list(sensors.keys())[idx]
    beac = sensors[sens]
    return manhattan_distance(sens, beac)



def search_row(y:int, sens:tuple, sb_dist:int):
    """Search row y for points which cannot be a beacon based on the current sensor.
    """
    points = []

    # if the distance between a sensor and the given point is less than
    # the distance between the sensor and its known beacon, then the point
    # cannot be a beacon since each sensor's known beacon is its closest
    x = 0
    while True: 
        # search to the right of the sensor, at row y
        p2 = (sens[0]+x, y)
        if manhattan_distance(sens, p2) <= sb_dist:
            points.append(p2)
            x += 1
        else:
            break

    x = 0
    while True: 
        # search to the left of the sensor, at row y
        p2 = (sens[0]+x, y)
        if manhattan_distance(sens, p2) <= sb_dist:
            points.append(p2)
            x -= 1
        else:
            break
    
    return points



# Extra:
def search_direction(sens:tuple, sb_dist:int, coord:str, sign:int=1) -> tuple:
    coord_inc = {'x':0,'y':0} ##increment coordinate position
    max_point = None

    while True:
        p2 = ( sens[0]+coord_inc['x'], sens[1]+coord_inc['y'] )
        if manhattan_distance(sens, p2) <= sb_dist:
            coord_inc[coord] += sign*1
        else:
            max_point = p2
            break
    return max_point

def find_impossible_positions(sensor_idx, sensors):
    """get complete list of impossible beacon positions for the given sensor, via brute force.
    """
    # sensor & beacon x,y positions, and distance
    sens = list(sensors.keys())[sensor_idx]
    beac = sensors[sens]
    dist = sensor_beacon_dist(sensor_idx, sensors)

    min_point   = search_direction(sens, dist, coord='y', sign=-1)
    max_point   = search_direction(sens, dist, coord='y', sign= 1)
    # right_point = search_direction(sens, dist, coord='x', sign= 1)
    # left_point  = search_direction(sens, dist, coord='x', sign=-1)

    points = []
    for y in range(min_point[1], max_point[1]+1): ##inclusive of max point
        points += search_row(y, sens, dist)

    return points

def draw_grid(not_beacons:list, sensors:dict):
    """Draw the grid (only feasible for the puzzle's example input)
    """
    beacons = sensors.values()
    xs = set([x for x,_ in not_beacons])
    ys = set([y for _,y in not_beacons])

    out = ""
    for row in range(min(ys), max(ys)+1):
        chars = f"{row :<} "
        for col in range(min(xs), max(xs)+1):
            if (col, row) in sensors:
                chars += "S"
            elif (col, row) in beacons:
                chars += "B"
            elif (col,row) in not_beacons:
                chars += "#"
            else:
                chars += "."
        out += chars + '\n'

    return out    



if __name__=="__main__":

    sensors = {}
    with open("advent-of-code/inputs/day15.txt") as f:
        for line in f:
            sens, beac = line.strip().split(":")

            sens_pos = [0,1]
            sens = sens.strip().split()
            for chunk in sens:
                chunk = ''.join(c for c in chunk.strip() if c in string.ascii_letters+string.digits)
                if chunk.startswith("x"):
                    sens_pos[0] = int( ''.join(c for c in chunk if c not in "x=") )
                if chunk.startswith("y"):
                    sens_pos[1] = int( ''.join(c for c in chunk if c not in "y=") )
            
            beac_pos = [0,1]
            beac = beac.strip().split()
            for chunk in beac:
                chunk = ''.join(c for c in chunk.strip() if c in string.ascii_letters+string.digits)
                if chunk.startswith("x"):
                    beac_pos[0] = int( ''.join(c for c in chunk if c not in "x=") )
                if chunk.startswith("y"):
                    beac_pos[1] = int( ''.join(c for c in chunk if c not in "y=") )
            
            sensors[(sens_pos[0], sens_pos[1])] = (beac_pos[0], beac_pos[1])

    sensor_ls = list(sensors.keys())
    beacon_ls = list(sensors.values())


    # PART 1
    ROW = 2_000_000

    nb = [] ##non-beacons
    for i in range(len(sensors)):
        sens = list(sensors.keys())[i]
        dist = sensor_beacon_dist(i, sensors)
        # search row for points which cannot be beacons
        nb += search_row(ROW, sens, dist)

    nb = [xy for xy in nb if xy not in beacon_ls]

    print("Part 1 tuning frequency:", len(set(nb)))



    # # to render the whole grid:
    # points = []
    # for i in range(len(sensors)):
    #     points += find_impossible_positions(i, sensors)

    # p = [(x,y) for x,y in points if y==ROW]
    # p = [xy for xy in p if xy not in sensor_ls+beacon_ls]
    # print(len(set(p)))
    # print(draw_grid(points, sensors))