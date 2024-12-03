#!/usr/bin/python3.11
from collections import Counter

# AOC 2023 day 7
# this is not pretty





def assign_rank_p1(hand: list[int]) -> int:
    handcnt = Counter(hand)
    num_mostcommon = handcnt.most_common(1)[0][1]
    nunique = len(handcnt)
    if nunique == 5:
        return 0 ## all diff cards
    elif nunique == 4:
        return 1 ## 1 pair
    elif nunique == 3:
        if num_mostcommon == 2:
            return 2 ## 2 pair
        if num_mostcommon == 3:
            return 3 ## 3 of a kind
    elif nunique == 2:
        if num_mostcommon == 3:
            return 4 ## full house
        elif num_mostcommon == 4:
            return 5 ## 4 of a kind
    else: # nunique == 1, 5 of a kind
        return 6
    return -1


def assign_rank_p2(hand: list[int]) -> int:
    jack = 1 # from scoremap2
    handcnt = Counter(hand)
    num_jacks = handcnt.get(jack, 0)
    card_mostcommon, num_mostcommon = handcnt.most_common(1).pop()
    nunique = len(handcnt)
    # deal with jacks
    if nunique == 1 and card_mostcommon == jack:
        return 6 ## 5 Jacks
    if card_mostcommon == 1:
        # if the most common card is Jack, pick the second most common
        card_mostcommon, num_mostcommon = handcnt.most_common(2).pop()
    if num_jacks > 0: # merge jacks with the highest count of other card
        num_mostcommon += num_jacks
        nunique -= 1
    # rank hand
    if nunique == 5:
        return 0 # 5 diff cards
    if nunique == 4:
        return 1 ## 1 pair
    elif nunique == 3:
        if num_mostcommon == 2:
            return 2 ## 2 pair
        if num_mostcommon == 3:
            return 3 ## 3 of a kind
    elif nunique == 2:
        if num_mostcommon == 3:
            return 4 ## full house
        elif num_mostcommon == 4:
            return 5 ## 4 of a kind
    else: # nunique == 1, 5 of a kind
        return 6
    return -1



scoremap1 = {c: i for i,c in enumerate("__23456789TJQKA")}
scoremap2 = {c: i for i,c in enumerate("_J23456789T_QKA")}

def _samerank_lt(hand0, hand1):
    cardix = 0
    while hand0[cardix] == hand1[cardix]:
        cardix += 1
    return True if hand0[cardix] < hand1[cardix] else False

class Hand:
    def __init__(self, hand: str, bid: int, part2: bool=False) -> None:
        self.bid = bid
        self.handstr = hand
        if part2:
            self.hand = [scoremap2[ch] for ch in hand]
            self.rank = assign_rank_p2(self.hand)
        else:
            self.hand = [scoremap1[ch] for ch in hand]
            self.rank = assign_rank_p1(self.hand)

    def __lt__(self, other_hand: object) -> bool:
        # implementing __lt__ allows for use of list.sort
        if self.rank == other_hand.rank:
            return _samerank_lt(self.hand, other_hand.hand)
        return self.rank < other_hand.rank



with open("input.txt", "r") as f:
    LINES = [line.split(" ") for line in f.read().split("\n")]
    hands = [l[0] for l in LINES]
    bids = [int(l[1]) for l in LINES]

def part1():
    rankedhands = [Hand(hand, bid) for hand, bid in zip(hands, bids)]
    rankedhands.sort()
    return sum([hand.bid * (rank + 1) for rank, hand in enumerate(rankedhands)])

def part2():
    rankedhands = [Hand(hand, bid, part2=True) for hand, bid in zip(hands, bids)]
    rankedhands.sort()
    return sum([hand.bid * (rank + 1) for rank, hand in enumerate(rankedhands)])


print("part 1 solution:", part1())
print("part 2 solution:", part2())