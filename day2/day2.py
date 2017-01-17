#!/usr/bin/env python3


def calculate_paper(instruction):
    l, w, h = tuple(map(int, instruction.split('x')))
    x, y, _ = sorted([l, w, h])

    return (2 * l * w) + (2 * w * h) + (2 * h * l) + (x * y)


def calculate_ribbon(instruction):
    l, w, h = tuple(map(int, instruction.split('x')))
    x, y, _ = sorted([l, w, h])

    return (l * w * h) + (2 * x) + (2 * y)


def total_paper(instructions):
    return sum(calculate_paper(x) for x in instructions)


def total_ribbon(instructions):
    return sum(calculate_ribbon(x) for x in instructions)


if __name__ == "__main__":

    with open('2.in', 'r') as f:
        instructions = f.read().splitlines()
    print(total_paper(instructions))

    assert total_paper(['2x3x4']) == 58, total_paper(['2x3x4'])
    assert total_paper(['1x1x10']) == 43, total_paper(['1x1x10'])

    assert total_ribbon(['2x3x4']) == 34, total_ribbon(['2x3x4'])
    assert total_ribbon(['1x1x10']) == 14, total_ribbon(['1x1x10'])

    print(total_ribbon(instructions))
