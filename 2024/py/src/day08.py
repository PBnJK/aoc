# Day 8: Resonant Collinearity

from collections import defaultdict
from itertools import permutations

from src import util

inp = util.input_lines("day08.txt")

SZ = range(len(inp[0]))

inpmap = defaultdict(set)
for i, li in enumerate(inp):
    for j, c in enumerate(li):
        if c != ".":
            inpmap[c].add((j, i))


# From: https://math.stackexchange.com/a/149337
def anti(x0, y0, x1, y1, t):
    return ((x1 - x0) * t + x0, (y1 - y0) * t + y0)


def dist(x0, y0, x1, y1, x2, y2):
    a = abs(x1 - x0) + abs(y1 - y0)
    b = abs(x2 - x0) + abs(y2 - y0)

    return a * 2 == b or b * 2 == a


def star1():
    antinodes = set()
    for v in inpmap.values():
        if len(v) == 1:
            continue

        for a, b in permutations(v, 2):
            i = 0
            while True:
                node = anti(*a, *b, i)
                if node[0] not in SZ or node[1] not in SZ:
                    break

                i += 1
                if not dist(*a, *b, *node):
                    continue

                antinodes.add(node)

    return len(antinodes)


def star2():
    antinodes = set()
    for v in inpmap.values():
        if len(v) == 1:
            continue

        for a, b in permutations(v, 2):
            i = 0
            while True:
                node = anti(*a, *b, i)
                if node[0] not in SZ or node[1] not in SZ:
                    break

                i += 1
                antinodes.add(node)

    return len(antinodes)


util.run_day(8, star1, star2)
