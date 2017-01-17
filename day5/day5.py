#!/usr/bin/env python3

"""

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
"""

def chk_3_vowels(line):
    vowels = 'aeiou'
    return sum((x == y) for y in line for x in vowels) >= 3


def duplicate(line):
    return any((line[pos] == line[pos + 1]) for pos in range(len(line) - 1))


def notcontains_pair(line):
    return not any( (x in line) for x in ('ab', 'cd', 'pq', 'xy') )


def calculate_part1(line):
    return all((chk_3_vowels(line), duplicate(line), notcontains_pair(line)))

"""
    Part 2

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
"""
from itertools import starmap
import re

def generate_pair_result(duplicate_pairs, s):
    for pair in duplicate_pairs:
        for m in re.finditer(pair, s):
            end_index = m.end()
            try:
                print(s[end_index] != s[end_index + 1])
                yield s[end_index] != s[end_index + 1]
            except IndexError:
                yield True

def appear_twiceold(s):
    # Split line into pairs
    z = list(zip(s[::2], s[1::2])) + list(zip(s[1::2], s[2::2]))
    pairs = list(starmap(lambda x,y: x+y, z))
    duplicate_pairs = [x for x in pairs if pairs.count(x) > 1]

    return any(generate_pair_result(duplicate_pairs, s))

def generate_pair_result2(duplicate_pairs, s):
    for pair in duplicate_pairs:
        end_index = None
        for m in re.finditer(pair, s):
            print(end_index == m.start())
            yield end_index == m.start()
            end_index = m.end()

def appear_twice(s):
    # Split line into pairs
    z = list(zip(s,s[1:]))
    pairs = list(starmap(lambda x,y: x+y, z))


    duplicate_pairs = [x for x in pairs if pairs.count(x) > 1]

    for pair in duplicate_pairs:
        for m in re.finditer(pair, s):
            indx = m.start()
            try:
                if s[indx] != s[indx + 2]:
                    return True
            except:
                # Index is out of range so there cannot be overlaps
                return True




def one_letter_btween(line):
    f = lambda x, y, z: (x == z) and (x != y)
    return any(f(line[i], line[i+1], line[i+2]) for i in range(len(line) -2))


def calculate_part2(line):
    return all((one_letter_btween(line.strip()), appear_twice(line.strip())))


def main_part1(lines):
    return sum(calculate_part1(x) for x in lines)

def main_part2(lines):
    return sum(calculate_part2(x) for x in lines)


if __name__ == "__main__":

    assert chk_3_vowels('aei')
    assert not chk_3_vowels('aizbv')


    assert duplicate('xxy')
    assert not duplicate('xyz')

    assert not notcontains_pair('abc')
    assert notcontains_pair('dbe')

    assert calculate_part1('ugknbfddgicrmopn')
    assert calculate_part1('aaa')
    assert not calculate_part1('jchzalrnumimnmhp')
    assert not calculate_part1('haegwjzuvuyypxyu')
    assert not calculate_part1('dvszwmarrgswjxmb')

    assert calculate_part2('qjhvhtzxzqqjkmpb')
    assert calculate_part2('xxyxx')
    assert not calculate_part2('uurcxstgmygtbstg')
    assert not calculate_part2('ieodomkazucvgmuy')
    assert not appear_twice('aaa')
    assert appear_twice('aaadcfaa')
    assert one_letter_btween('aaabcdeaxa')
    assert not one_letter_btween('aaabcdeaa')
    assert one_letter_btween('aaabcdeaba')

    with open('5.in', 'r') as f:
        lines = f.read().splitlines()
        print(main_part1(lines))
        print(main_part2(lines)) # 59 too high, 52 too low == 55
