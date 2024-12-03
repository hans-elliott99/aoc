#!/usr/bin/env python3

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 8: Treetop Tree House
# hans elliott

import numpy as np
import math        
import sys
import matplotlib.pyplot as plt

def vis_from_rows(grid:np.array, visible:np.array) -> np.array:
    """Update 'visible' matrix at elements which can be seen from outside grid,
    viewing row-wise.
    """
    for ri in range(grid.shape[0]):
        row = grid[ri,:].tolist()

        for j, tr in enumerate(row):
            if (j == 0) | (j == grid.shape[1]-1): 
                visible[ri, j] = 1 ##border
            elif (max(set(row[:j])) < tr) | (max(set(row[j+1:])) < tr):
                visible[ri, j] = 1
    
    return visible

def vis_from_cols(grid:np.array, visible:np.array) -> np.array:
    """Update 'visible' matrix at elements which can be seen from outside grid,
    viewing col-wise.
    """
    for cj in range(grid.shape[1]):
        col = grid[:, cj].tolist()

        for i, tr in enumerate(col):
            if (i == 0) | (i == grid.shape[0]-1): 
                visible[i, cj] = 1 ##border
            elif (max(set(col[:i])) < tr) | (max(set(col[i+1:])) < tr):
                visible[i, cj] = 1
    
    return visible

def calc_scenic_score(grid:np.array) -> np.array:
    """Calculate the scenic score for each tree, ie the product of the
    viewing distance in each cardinal direction.
    """
    scores = np.zeros_like(grid)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            candidate_tree = grid[i,j]
            
            above = grid[:, j][:i  ].tolist()
            below = grid[:, j][i+1:].tolist()
            left  = grid[i, :][:j  ].tolist()
            right = grid[i, :][j+1:].tolist()
            
            view_dists = []
            # Iterate through each of the directions and compare tree heights.
            # Reverse 'above' & 'left' in order to compare closer trees first.
            for ray in [above[::-1], below, left[::-1], right]:
                vd = 0
                if ray: ##if on edge, 'ray' can be empty and then view dist=0
                    for t in ray:
                        vd += 1
                        if t >= candidate_tree:
                            break
                view_dists.append(vd)

            assert len(view_dists) == 4
            scores[i,j] = math.prod(view_dists)
    return scores


if __name__=="__main__":

    # parse input text
    grid = []
    with open("advent-of-code/inputs/day8.txt") as f:
        for line in f:
            grid.append( [int(x) for x in line.strip()] )
    grid = np.array(grid)    
    
    # Part 1: Find total number of trees visible from outside of the grid
    #         (only visible if no taller trees between tree i and the edge)
    visible = np.zeros_like(grid)
    visible = vis_from_cols(grid, vis_from_rows(grid, visible))
    
    # Part 2: Find the largest "scenic score" - the product of the viewing
    #          distances in each direction (left,right,up,down) from tree i
    score = calc_scenic_score(grid)

    print(f"Part 1: Total trees visible from outside grid:", sum(visible[visible==1]) )
    print(f"Part 2: Largest scenic score of any tree:",      np.amax(score) )


    if len(sys.argv) > 1:
        plt.figure(figsize=(10,5))

        plt.subplot(121)
        plt.title("Trees visible from forest edge")
        plt.imshow(visible, cmap="summer")
        plt.axis('off')

        plt.subplot(122)
        plt.title("Scenic score per tree")
        plt.imshow(score, cmap="copper")
        plt.axis('off')

        plt.show()


