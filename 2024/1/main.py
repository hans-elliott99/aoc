# AOC 2024 Day 1

left = []
right = []

with open("./input.txt", "r") as f:
    for line in f:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

left = sorted(left)
right = sorted(right)
assert len(left) == len(right)

# Part 1: sum of distances of sorted numbers
distances = [abs(left[i] - right[i]) for i in range(len(left))]
print(f"Part 1 solution: {sum(distances)}")

# Part 2: similarity score
score = 0
for i in left:
    score += i * right.count(i)
print(f"Part 2 solution: {score}")

