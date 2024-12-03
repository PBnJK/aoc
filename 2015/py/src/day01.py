# Day 01: Not Quite Lisp


from src import util


def star1():
    floor: int = 0
    for c in util.input_single("day01.txt"):
        floor += 1 if c == "(" else -1

    return floor


def star2():
    floor: int = 0
    for e, c in enumerate(util.input_single("day01.txt"), start=1):
        floor += 1 if c == "(" else -1
        if floor == -1:
            return e

    return 0
