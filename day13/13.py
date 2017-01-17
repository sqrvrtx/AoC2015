s = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""
import re
from itertools import *
f = lambda w,x,y,z: (w, z, int(y)*-1) if x == 'lose' else (w, z, int(y))
st = set()
d = {}

s = open('13.in').read()
for line in s.splitlines():
    out = re.search(r'(\w+) \w+ (\w+) (\d+).* (\w+)', line).groups()
    a,b, val = f(*out)
    st.update([a,b])
    d[(a,b)] = val
perms = [p for p in permutations(st, len(st))]

print perms
def genperms(perms):
  for a in perms:
    pairs = zip(a, a[1:]+a[:1])
    cnt =0
    for pair in pairs:
        x,y = pair
        val = d[(x,y)] + d[(y,x)]
        cnt += val
    yield cnt
wome= max(genperms(perms))

mels = map(lambda x: ('Me', x) , st) + map(lambda x: (x, 'Me') , st)

from collections import defaultdict
dd = defaultdict(int)
print [dd[x] for x in mels]
print dd
d.update(dd)
st.add('Me')
perms = [p for p in permutations(st, len(st))]
for p in perms:
    print(p)

wime = max(genperms(perms))

print wime  # 601
