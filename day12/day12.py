#!/usr/bin/env python3
import re
import json


s = open('12.in').read()
nums = re.findall(r'(-?\d+)',s)
print(sum(int(x) for x in nums))  # 119433


# Part 2

def main(x):

    if isinstance(x, int):
        yield x
    elif isinstance(x, list):
        for val in x:
            yield from main(val)
    elif isinstance(x, dict):
        if "red" not in x.values():
            for val in x.values():
                yield from main(val)

# Tests
t1 = [1,2,3]
t2 = [1,{"c":"red","b":2},3]
t3 = {"d":"red","e":[1,2,3,4],"f":5}
t4 = [1,"red",5]

t5 = [1,{"c":"blue","b":2, "c":[1,2,3]},3]

assert sum(main(t1)) == 6
assert sum(main(t2)) == 4
assert sum(main(t3)) == 0
assert sum(main(t4)) == 6
assert sum(main(t5)) == 12, sum(main(t5))

# Actual
py_objs = json.loads(s)
print(sum(main(py_objs)))  # 68466
