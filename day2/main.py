import re
import os
path = os.path.dirname(os.path.realpath(__file__))

with open(f'{path}/input.txt') as f:
    inputs = f.read().strip().split('\n')

class Password(object):
    def __init__(self, line: str):
        m = re.search(r"(\d+)-(\d+) ([a-z]): ([a-z]*)", line)
        self.min = int(m.group(1))
        self.max = int(m.group(2))
        self.char = m.group(3)
        self.password = m.group(4)

    def is_valid(self):
        count = self.password.count(self.char)
        is_valid = count >= self.min and count <= self.max

        if not is_valid:
            print(f"invalid: {self}")

        return is_valid


    def __str__(self):
        return str({"min": self.min, "max": self.max, "char": self.char, "password": self.password})

print(sum(map(lambda line: Password(line).is_valid(), inputs)))
