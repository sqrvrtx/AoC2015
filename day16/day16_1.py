#!/usr/bin/env python

import re

ticker_tape = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""


def split_func(s):
    x, y = s.split(': ')
    return x, y


st = {split_func(x) for x in ticker_tape.splitlines()}


def part_one(lines):
    for line in lines:
        td = [split_func(x) for x in list(line)[1:]]

        if st.issuperset(td):
            return(list(line)[0])


def main(lines):
    rtn = []
    for line in lines:
        rtn.append(re.search(r'(\d+): (\w+: \d+), (\w+: \d+), (\w+: \d+)', line).groups())

    return rtn


if __name__ == "__main__":
    with open('16.in', 'r') as f:
        lines = main(f.read().splitlines())  # 373
    print(part_one(lines))
