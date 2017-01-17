from itertools import *


test_containers= [20, 15, 10, 5, 5]
containers = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]


def calculate(containers, total):
    lenc = len(containers)

    val = lenc
    while val > 0:
        combs = combinations(containers, val)
        yield sum([(sum(y)  == total) for y in combs])
        val -= 1


def main(containers, total_volume):
    print(sum(calculate(containers, total_volume)))


if __name__ == "__main__":
    main(test_containers, 25)
    main(containers, 150)
