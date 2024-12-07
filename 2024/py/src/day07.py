# Day 7: Bridge Repair

from src import util

# from itertools import product, chain, zip_longest

inp = [
    (int(y[0]), [int(z) for z in y[1].split()])
    if (y := x.strip().split(": "))
    else (0, [])
    for x in util.input_lines("day07.txt")
]


def star1():
    total = 0
    for n, m in inp:
        m = m.copy()
        m.reverse()

        def proc(stack):
            if len(stack) == 1:
                return n if stack.pop() == n else 0

            lhs, rhs = stack.pop(), stack.pop()

            s = stack.copy()
            s.append(lhs + rhs)
            if proc(s) != 0:
                return n

            s = stack.copy()
            s.append(lhs * rhs)
            if proc(s) != 0:
                return n

            return 0

        total += proc(m)

    return total


def star2():
    total = 0
    for n, m in inp:
        m = m.copy()
        m.reverse()

        def proc(stack):
            if len(stack) == 1:
                return n if stack.pop() == n else 0

            lhs, rhs = stack.pop(), stack.pop()

            s = stack.copy()
            s.append(lhs + rhs)
            if proc(s) != 0:
                return n

            s = stack.copy()
            s.append(lhs * rhs)
            if proc(s) != 0:
                return n

            s = stack.copy()
            s.append(int(str(lhs) + str(rhs)))
            if proc(s) != 0:
                return n

            return 0

        total += proc(m)

    return total


util.run_day(7, star1, star2)