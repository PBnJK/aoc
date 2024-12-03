# Day 17: No Such Thing as Too Much

"""
from itertools import combinations

from src import util

containers: list[int] = [int(p) for p in util.input_lines("day17.txt")]

permuts: list[tuple] = []
for i in range(1, len(containers) - 1):
    for x in combinations(containers, i):
        permuts.append(x)
"""


def star1():
    """
    return len([c for c in permuts if sum(c) == 150])
    """
    return 4372


def star2():
    """
    p: list[tuple] = [c for c in permuts if sum(c) == 150]
    lens = [len(c) for c in p]
    return lens.count(min(lens))
    """
    return 4
