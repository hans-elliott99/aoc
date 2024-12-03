#!/usr/bin/python3.11



with open("input.txt", "r") as f:
    lines = f.readlines()

game_id_sum = 0
for line in lines:
    line = line.strip()
    game, sets = line.split(":")
    game = int(game.split(" ")[-1])
    sets = sets.strip().split(";")

    for draw in sets:
        fail = False
        cubes = draw.split(",")
        for cube in cubes:
            n, color = cube.strip().split(" ")
            n = int(n.strip())
            color = color.strip()
            if (color == "red" and n > 12
                or color == "green" and n > 13
                or color == "blue" and n > 14):
                fail = True
                break
        # if one set fails, the whole game failes
        if fail:
            game = 0
            break
    
    game_id_sum += game

print(f"sum of successful game ids = {game_id_sum}")