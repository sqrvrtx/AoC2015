#!/usr/bin/env python3

"""
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""
from itertools import *

s = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""

import re
from operator import itemgetter

def main(lines):
    cities = set()
    d = {}
    for line in lines:
        c1, c2 , dist = re.match(r'(\w+) to (\w+) = (\d+)', line).groups()
        d[(c1, c2)] = dist
        cities.update(set([c1, c2]))
    print(cities)
    nd = {}
    dd={}
    for k in d:
        x,y = k
        dd[(y,x)] = d[k]
        dd[k] = d[k]

    for tpl in (list(permutations(cities, len(cities)))):
        count=0
        for i in range(len(tpl) -1):
            count += int(dd[(tpl[i], tpl[i+1])])

        nd[tpl] = count#int(dd[(x,y)]) + int(dd[(y,z)])
    #print(nd)
    return "Min: %r, \nMax %r" % (min(nd.items(), key=itemgetter(1)), \
                                  max(nd.items(), key=itemgetter(1)))


lines = s.splitlines()
print(main(lines))

with open('9.in', 'r') as f:
    print(main(f.read().splitlines()))
