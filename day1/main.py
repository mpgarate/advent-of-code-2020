from collections import Counter

import os
path = os.path.dirname(os.path.realpath(__file__))

with open(f'{path}/input.txt') as f:
    inputs = f.read().strip().split('\n')

input_counts = Counter(map(lambda l: int(l), inputs))

target = 2020

def part1(input_counts):
    for n in input_counts:
        candidate = target - n

        # ensure 'n' is not considered a candidate unless it appears twice in input
        threshold = 1 if not target - n == n else 2

        if input_counts[candidate] >= threshold:
            return n * candidate


def part2(input_counts):
    for n1 in input_counts:
        for n2 in input_counts:
            candidate = (target - n1) - n2

            # ensure any 'n' is not considered a candidate unless it appears twice in input
            threshold = sum(1 if n == candidate else 0 for n in [n1, n2]) + 1

            if input_counts[candidate] >= threshold:
                return n1 * n2 * candidate

print("=== part 1 ===")
print(part1(input_counts))

print("=== part 2 ===")
print(part2(input_counts))
