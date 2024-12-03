# Day 09: All in a Single Night

# I have a confession to make: I cheated on this one
#
# As such, I will write a very long explanation to prove that I didn't just
# pull this off of the net without bothering to understand it.
#
# First off: why *couldn't* I solve this?
#
# Well, there is a fact that is very useful in solving this problem that I just
# didn't catch. Namely:
#
#    "All cities connect to each other"
#
# This allows us to build a set of cities and be *sure* that all permutations
# of that set are valid paths.
#
# Also, as a bonus, I'm not very experienced in Python. I didn't even *know*
# that sets were a built-in data structure! I knew dicts, lists and tuples,
# sure, but sets?! That's new!
#
# So yeah; my mistake.
#
# But enough dawdling: how did the very clever u/shandelman solve this?
#
# The step-by-step is this:
# 1. Built two data structures: a set with all cities, and a weighted graph
#    that maps the paths between each city (LINES 45-55);
# 2. Run through every permutation of the cities set and sum the distances
#    between each pair of cities travelled, visiting every city in the process,
#    and build a list of all distances (LINES 57-59);
# 3. Take the shortest (or longest for star 2) distance from the distance list:
#    that's your solution (star1/star2)
#
# It's simple; *dead* simple. I'm kind of embarassed I couldn't solve it. But
# you live and you learn. I'm 17; I have much to learn.
#
# Here's the original solution if you wish to see it:
# https://old.reddit.com/r/adventofcode/comments/3w192e/day_9_solutions/cxstkax/


from src import util
from itertools import permutations

cities: set[str] = set()
dists: dict[str, dict[str, int]] = {}

for path in util.input_lines("day09.txt"):
    start, _, end, _, dist = path.split()

    cities.add(start)
    cities.add(end)

    dists.setdefault(start, {})[end] = int(dist)
    dists.setdefault(end, {})[start] = int(dist)

paths: list[int] = []
for p in permutations(cities):
    paths.append(sum([dists[start][end] for start, end in zip(p, p[1:])]))


def star1():
    return min(paths)


def star2():
    return max(paths)
