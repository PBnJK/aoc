# Day 03: Perfectly Spherical Houses in a Vacuum


from src import util

TABLE = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}


def star1():
    visited: set[tuple[int, int]] = {(0, 0)}

    x, y = 0, 0
    for c in util.input_single("day03.txt"):
        t = TABLE[c]
        x += t[0]
        y += t[1]

        visited.add((x, y))

    return len(visited)


def star2():
    visited: set[tuple[int, int]] = {(0, 0)}

    sx, sy = 0, 0
    rx, ry = 0, 0
    turn = False
    for c in util.input_single("day03.txt"):
        t = TABLE[c]
        if turn:
            sx += t[0]
            sy += t[1]
            visited.add((sx, sy))
        else:
            rx += t[0]
            ry += t[1]
            visited.add((rx, ry))

        turn = not turn

    return len(visited)
