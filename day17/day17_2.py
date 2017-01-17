from itertools import *


test_containers= [20, 15, 10, 5, 5]
containers = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]


def calculate(containers, total):
    lenc = len(containers)

    val = 0
    while val < lenc:
        combs = combinations(containers, val)
        z = sorted(y for y in combs if sum(y)  == total)
        if z:
            yield len(z)
            break
        val += 1


def main(containers, total_volume):
    print(list(calculate(containers, total_volume)))


if __name__ == "__main__":
    main(test_containers, 25)
    main(containers, 150)
