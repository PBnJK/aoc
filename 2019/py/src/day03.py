# Day 3: Crossed Wires

from src import util

d1, d2 = util.input_lines("day03.txt")
d1 = d1.strip().split(",")
d2 = d2.strip().split(",")


def getmove(move):
    return move[0], int(move[1:])


def star1():
    visited = {(0, 0)}
    endings = set()

    x, y = 0, 0
    for move in d1:
        move = getmove(move)

        tx, ty = x, y
        match move[0]:
            case "U":
                ty = y - move[1]
            case "D":
                ty = y + move[1]
            case "L":
                tx = x - move[1]
            case "R":
                tx = x + move[1]

        if ty == y:
            if tx > x:
                r = range(x, tx + 1)
            else:
                r = range(x, tx - 1, -1)

            for i in r:
                visited.add((i, y))
        else:
            if ty > y:
                r = range(y, ty + 1)
            else:
                r = range(y, ty - 1, -1)

            for i in r:
                visited.add((x, i))

        x, y = tx, ty

    x, y = 0, 0
    for move in d2:
        move = getmove(move)

        tx, ty = x, y
        match move[0]:
            case "U":
                ty = y - move[1]
            case "D":
                ty = y + move[1]
            case "L":
                tx = x - move[1]
            case "R":
                tx = x + move[1]

        if ty == y:
            if tx > x:
                r = range(x, tx + 1)
            else:
                r = range(x, tx - 1, -1)

            for i in r:
                p = (i, y)
                if p in visited:
                    endings.add(p)
        else:
            if ty > y:
                r = range(y, ty + 1)
            else:
                r = range(y, ty - 1, -1)

            for i in r:
                p = (x, i)
                if p in visited:
                    endings.add(p)

        x, y = tx, ty

    endings.remove((0, 0))
    return min([(abs(ix) + abs(iy)) for ix, iy in endings])


def star2():
    v1, v2 = {(0, 0)}, {(0, 0)}
    w1, w2 = [], []

    x, y = 0, 0
    for move in d1:
        move = getmove(move)

        tx, ty = x, y
        match move[0]:
            case "U":
                ty = y - move[1]
            case "D":
                ty = y + move[1]
            case "L":
                tx = x - move[1]
            case "R":
                tx = x + move[1]

        if ty == y:
            if tx > x:
                r = range(x, tx)
            else:
                r = range(x, tx, -1)

            for i in r:
                p = (i, y)
                v1.add(p)
                w1.append(p)
        else:
            if ty > y:
                r = range(y, ty)
            else:
                r = range(y, ty, -1)

            for i in r:
                p = (x, i)
                v1.add(p)
                w1.append(p)

        x, y = tx, ty

    w1.append((x, y))

    x, y = 0, 0
    for move in d2:
        move = getmove(move)

        tx, ty = x, y
        match move[0]:
            case "U":
                ty = y - move[1]
            case "D":
                ty = y + move[1]
            case "L":
                tx = x - move[1]
            case "R":
                tx = x + move[1]

        if ty == y:
            if tx > x:
                r = range(x, tx)
            else:
                r = range(x, tx, -1)

            for i in r:
                p = (i, y)
                v2.add(p)
                w2.append(p)
        else:
            if ty > y:
                r = range(y, ty)
            else:
                r = range(y, ty, -1)

            for i in r:
                p = (x, i)
                v2.add(p)
                w2.append(p)

        x, y = tx, ty

    w2.append((x, y))

    endings = v1 & v2
    endings.remove((0, 0))

    tot = set()
    for e in endings:
        tot.add(w1.index(e) + w2.index(e))

    return min(tot)
