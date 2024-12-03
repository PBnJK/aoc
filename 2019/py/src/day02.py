# Day 2: 1202 Program Alarm

from src import util, intcode


data = [int(i) for i in util.input_single("day02.txt").split(",")]


def star1():
    intc = intcode.IntCode(data)
    intc.insert(1, 12)
    intc.insert(2, 2)

    return intc.run()


def star2():
    intc = intcode.IntCode(data)

    for i in range(100):
        for j in range(100):
            intc.insert(1, i)
            intc.insert(2, j)

            if intc.run() == 19690720:
                return 100 * i + j
