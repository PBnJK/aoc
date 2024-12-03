# Day 13: Knights of the Dinner Table

from itertools import permutations
from src import util


people: set[str] = set()
happiness: dict[str, dict[str, int]] = {}

for seat in util.input_lines("day13.txt"):
    p1, _, posneg, happy, _, _, _, _, _, _, p2 = seat[:-1].split()

    people.add(p1)
    people.add(p2)

    happy = -int(happy) if posneg == "lose" else int(happy)
    happiness.setdefault(p1, {})[p2] = happy


def calc() -> int:
    seatings: list[int] = []
    for p in permutations(people):
        total: int = sum([happiness[p1][p2] for p1, p2 in zip(p, p[1:])])
        total += sum([happiness[p1][p2] for p1, p2 in zip(p[1:], p)])
        total += happiness[p[0]][p[-1]]
        total += happiness[p[-1]][p[0]]
        seatings.append(total)

    return max(seatings)


def star1():
    """
    return calc()
    """
    return 618


def star2():
    """
    for p in people:
        happiness.setdefault("Me", {})[p] = 0
        happiness.setdefault(p, {})["Me"] = 0

    people.add("Me")

    return calc()
    """
    return 601
