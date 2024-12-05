# Day 4: Secure Container

from src import util

r = util.input_single("day04.txt").split("-")
r = range(int(r[0]), int(r[1]) + 1)


def star1():
    valid = 0
    for p in r:
        p = str(p)

        last = "0"
        v = True
        has = False
        for c in p:
            if last == c:
                has = True

            if int(last) <= int(c):
                last = c
                continue

            v = False
            break

        if has and v:
            valid += 1

    return valid


def star2():
    valid = 0
    for p in r:
        p = str(p)

        last = "0"
        v = True
        has = False
        for i, c in enumerate(p):
            if (not has) and (last == c):
                has = True

            if int(last) <= int(c):
                last = c
                continue

            v = False
            break

        if has and v:
            valid += 1

    return valid
