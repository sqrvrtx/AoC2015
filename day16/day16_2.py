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
    return x, int(y)

st = {split_func(x) for x in ticker_tape.splitlines()}
dst = dict(st)
cats = int(dst.get('cats'))
trees = int(dst.get('trees'))
pomeranians = int(dst.get('pomeranians'))
goldfish = int(dst.get('goldfish'))

def part_one(lines):
    for line in lines:
        td = [split_func(x) for x in list(line)[1:]]

        if st.issuperset(td):
            return("TD1",list(line)[0],td)

def part_twofilter(dtd):

    ndtd = {k: v for k,v in dtd.items() if k not in ['cats', 'trees', 'pomeranians', 'goldfish']}

    if ((dtd.get('cats') is None or dtd.get('cats') > cats) and
       (dtd.get('trees') is None or dtd.get('trees') > trees) and
       (dtd.get('pomeranians') is None or dtd.get('pomeranians') < pomeranians) and
       (dtd.get('goldfish') is None or dtd.get('goldfish') < goldfish) and
       (st.issuperset(ndtd.items()))
       ):
          return dtd




def part_two(lines):
    for line in lines:
        td = [split_func(x) for x in list(line)[1:]]

        dtd = dict(td)
        dtd = {k: int(v) for k,v in dtd.items()}
        print td
        res = part_twofilter(dtd)
        if res:
            yield("TD2",list(line)[0],td)
    # z = [split_func(x) for y in lines for x in list(y)[1:]]
    # print z
    # print [part_twofilter(y) for y in dict(z)]

def main(lines):
    rtn = []
    for line in lines:
        rtn.append(re.search(r'(\d+): (\w+: \d+), (\w+: \d+), (\w+: \d+)', line).groups())

    return rtn


if __name__ == "__main__":
    with open('16.in', 'r') as f:
        lines = main(f.read().splitlines())

    print('##################')
    print(list(part_two(lines)))  # 260
