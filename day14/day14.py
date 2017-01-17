#!/usr/bin/env python3
s1 = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""

s2 = """Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.
"""

import re
from collections import namedtuple
from operator import attrgetter


class Reindeer:

    def __init__(self, *args):
        self.distance_travelled = 0
        self.points = 0
        self.name, self.speed, self.timetravel, self.timerest = args

    def __repr__(self):
        return "%s %d" % (self.name, self.distance_travelled)

    def increment(self, time_elapsed):
        mod_time_elapsed = time_elapsed % (int(self.timetravel) + int(self.timerest))
        if mod_time_elapsed < int(self.timetravel):
            self.distance_travelled += int(self.speed)


    def __iadd__(self, other=1):
        self.points += 1


def main(count_max, s):
    deers = []
    for line in s.splitlines():
        out = re.match(r'^(\w+) .* (\d+) .* (\d+) .* (\d+) ', line).groups()
        #print(out)
        deers.append(Reindeer(*out))
    count = 0
    while count <= count_max:

        [deer.increment(count) for deer in deers]
        max_len = max([deer for deer in deers], key=attrgetter('distance_travelled')).distance_travelled

        # Find all deers with max_len and increment
        [x.increment_points() for x in deers if x.distance_travelled == max_len]


        count += 1
    for deer in deers:
        print(deer.points, deer.distance_travelled)
    return max(deers, key=attrgetter('distance_travelled')), max(deers, key=attrgetter('points')).points


print(main(2503, s2)) # 2640 and 1102
