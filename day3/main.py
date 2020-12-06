import math
import os
path = os.path.dirname(os.path.realpath(__file__))

with open(f'{path}/test.txt') as f:
    inputs = f.read().strip().split('\n')

trees = map(lambda line: [True if c == '#' else False for c in line], inputs)

class Slope(object):
    def __init__(self, right, down):
        self.right = right
        self.down = down

        self.row = 0
        self.col = 0
        self.trees = 0

    def step(self, max_col):
        col = self.col + self.right

        self.col = col if col < max_col else col - max_col

        self.row += self.down

    def increment(self):
        self.trees += 1


slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]

for i, row in enumerate(trees):
    for slope in slopes:
        if slope.row != i:
            continue

        if row[slope.col] == True:
            slope.increment()

        slope.step(max_col = len(row))

print(math.prod([s.trees for s in slopes]))
