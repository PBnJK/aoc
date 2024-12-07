# Day 2: Red-Nosed Reports

from src import util


def diff(a):
    return [a[x] - a[x + 1] for x in range(len(a) - 1)]


DATA = util.input_lines("day02.txt")


def star1():
    safe = 0
    for line in DATA:
        if not line:
            break

        dline = diff([int(x) for x in line.split()])
        if (all(x < 0 for x in dline) or all(x > 0 for x in dline)) and abs(
            max(dline, key=abs)
        ) <= 3:
            safe += 1

    return safe


def star2():
    safe = 0
    for line in DATA:
        if not line:
            break

        line = [int(x) for x in line.split()]
        for i in range(len(line)):
            nl = line[:i] + line[i + 1 :]
            dline = diff(nl)
            if (all(x < 0 for x in dline) or all(x > 0 for x in dline)) and abs(
                max(dline, key=abs)
            ) <= 3:
                safe += 1
                break

    return safe


util.run_day(2, star1, star2)
