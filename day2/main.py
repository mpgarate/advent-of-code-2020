import re
import os
path = os.path.dirname(os.path.realpath(__file__))

with open(f'{path}/input.txt') as f:
    inputs = f.read().strip().split('\n')

class Password(object):
    def __init__(self, line: str):
        m = re.search(r"(\d+)-(\d+) ([a-z]): ([a-z]*)", line)
        self.n1 = int(m.group(1))
        self.n2 = int(m.group(2))
        self.char = m.group(3)
        self.password = m.group(4)

    def is_valid_policy_1(self):
        count = self.password.count(self.char)
        is_valid = count >= self.n1 and count <= self.n2

        if not is_valid:
            print(f"invalid: {self}")

        return is_valid

    def is_valid_policy_2(self):
        pw = {i+1: c for i, c in enumerate(self.password)}

        num_matches = sum([pw.get(self.n1, None) == self.char, pw.get(self.n2, None) == self.char])

        is_valid = num_matches == 1

        if not is_valid:
            print(f"invalid: {self}")

        return is_valid


    def __str__(self):
        return str({"n1": self.n1, "n2": self.n2, "char": self.char, "password": self.password})

print(sum(map(lambda line: Password(line).is_valid_policy_2(), inputs)))
