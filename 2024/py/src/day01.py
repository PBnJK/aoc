# Day 1: Historian Hysteria

from src import util


def sep():
    txt = util.input_lines("day01.txt")

    id1, id2 = [], []
    for line in txt:
        if not line:
            break

        a, b = line.strip().split("   ")
        id1.append(int(a))
        id2.append(int(b))

    return id1, id2


def star1():
    id1, id2 = sep()
    id1.sort()
    id2.sort()

    sum = 0
    for a, b in zip(id1, id2):
        sum += abs(a - b)

    return sum


def star2():
    id1, id2 = sep()

    sum = 0
    for a in id1:
        sum += a * id2.count(a)

    return sum


util.run_day(1, star1, star2)
