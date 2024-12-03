# Day 1: The Tyranny of the Rocket Equation

from src import util

data = util.input_lines("day01.txt")


def star1():
    total = sum([(int(m) // 3 - 2) for m in data])
    return total


def star2():
    total = 0
    for m in data:
        m = int(m)
        while True:
            m = m // 3 - 2
            if m <= 0:
                break

            total += m

    return total
