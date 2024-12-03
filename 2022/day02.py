#!/usr/bin/env python

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 2: Rock Paper Scissors
# hans elliott

import sys

# shape identifier / score conversion
rock = 1
paper = 2
scissors = 3

# maps
them2rps = {"A" : rock, "B" : paper, "C" : scissors} ## for both parts, map from character to shape
you2rps = {"X" : rock, "Y" : paper, "Z" : scissors} ## for part 1, map from character to shape

you2outcome = {"X" : "l", "Y" : "d", "Z" : "w" } ## for part 2, map from character to desired outcome
them2ulose = {rock : scissors, paper : rock, scissors : paper} ## for part 2, map from their move to your losing move
them2uwin = {rock : paper, paper : scissors, scissors : rock} ## for part 2, map from their move to your winning move

tostr = {1 : "rock", 2 : "paper", 3: "scissors"} ## for debugging


# PART 1
# Determine what shape they play given the input string.
# Determine what shape you play given the input string.
# Your total score is the outcome score plus the shape score, so:
# If you draw, you get 3 points for the outcome and n points for the shape.
# Otherwise, evaluate who wins the non-tie by checking a few conditions and then
#            add the approriate outcome score and shape score to your total score.
def eval_nontie(them_rps : int, you_rps : int) -> bool:
    if (them_rps==rock) & (you_rps==paper):
        return True
    elif (them_rps==paper) & (you_rps==scissors):
        return True    
    elif (them_rps==scissors) & (you_rps==rock):
        return True
    return False

def get_outcome_score(them_: str, you_: str) -> int:
    them = them2rps[them_]
    you = you2rps[you_]

    # Get outcome score (0 if lose, 3 if draw, 6 if win)
    score = 0
    win = False
    if you==them:
        score += 3
    else:
        win = eval_nontie(them, you)
        if win:
            score += 6
        else:
            score += 0
    # Add the score for the selected shape
    score += you

    # print(f"You: {tostr[you]}. Them: {tostr[them]}. Score: {score}. win {win}")
    return score



# PART 2
# Determine what shape they are playing given the input string
# Determine what outcome you need given the input string
# if You need to draw, your shape matches theirs and your score adjusts appropriately
# if You need to win, your shape matches the necessary winning shape, given their shape
# if You need to lose, your shape matches the necessary losing shape, given their shape
def get_outcome_score_part2(them_:str, you_:str) -> int:
    them = them2rps[them_]
    you_outcome = you2outcome[you_]

    score = 0
    if you_outcome == 'd':
        you=them
        score += 3 + you
    if you_outcome == 'w':
        you=them2uwin[them]
        score += 6 + you
    if you_outcome == 'l':
        you=them2ulose[them]
        score += 0 + you
    
    # print(f"You: {tostr[you]}. Them: {tostr[them]}. Score: {score}. Desired Outcome: {you_outcome}")
    return score

  

    

if __name__=="__main__":

    score_part1 = 0
    score_part2 = 0

    with open(sys.argv[1], 'r') as f:
        for line in f:
            l = line.strip().split(' ')
            them_, you_ = l[0], l[1]
            score_part1 += get_outcome_score(them_, you_)
            score_part2 += get_outcome_score_part2(them_, you_)

    print(f"Part 1 total score: {score_part1}")
    print(f"Part 2 total score: {score_part2}")