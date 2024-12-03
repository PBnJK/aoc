# Day 01: No Time for a Taxicab

import util

from collections import deque


def star1():
    i = util.input_single("day01.txt").split(", ")

    x: int = 0
    y: int = 0
    v: deque = deque([1, 0, 0, 0])
    for s in i:
        if s[0] == "L":
            v.rotate(-1)
        else:
            v.rotate()

        a: int = int(s[1:])
        y += v[0] * a
        x += v[1] * a
        y -= v[2] * a
        x -= v[3] * a

    return x + y


def star2():
    i = util.input_single("day01.txt").split(", ")

    visited: set[tuple[int, int]] = set()
    x: int = 0
    y: int = 0
    v: deque = deque([1, 0, 0, 0])
    print(i)
    for s in i:
        if s[0] == "L":
            v.rotate(-1)
        else:
            v.rotate()

        ox: int = x
        oy: int = y

        a: int = int(s[1:])
        y += v[0] * a
        x += v[1] * a
        y -= v[2] * a
        x -= v[3] * a

        if (x, y) in visited:
            print(f"{x, y} in visited")
            break

        print(f"{x, y} not")

        if x > ox:
            for mx in range(ox, x + 1):
                print(f"x {(mx, y)}")
                visited.add((mx, y))
        else:
            for mx in range(x, ox + 1):
                print(f"x {(mx, y)}")
                visited.add((mx, y))

        if y > oy:
            for my in range(oy, y + 1):
                print(f"y {(x, my)}")
                visited.add((x, my))
        else:
            for my in range(y, oy + 1):
                print(f"y {(x, my)}")
                visited.add((x, my))

    return x + y
