#!/usr/bin/python3.11


with open("input.txt", "r") as f:
    LINES = f.read().split("\n")

def get_card_nwins():
    nwins = []
    for card in LINES:
        _, numsets = card.split(": ")
        wins, nums = numsets.split(" | ")
        wins = [int(n) for n in wins.split()]
        nums = [int(n) for n in nums.split()]
        nums = [n for n in nums if n in wins]
        nwins.append(len(nums))
    return nwins

def part1():
    return sum([2 ** (n - 1) for n in get_card_nwins() if n > 0])

def part2():
    nwins = get_card_nwins()
    cards = [0 for _ in range(len(LINES))]
    for i in range(len(LINES)):
        cards[i] += 1
        for j in range(i + 1, i + nwins[i] + 1):
            cards[j] += cards[i]
    return sum(cards)


print(part1())
print(part2())