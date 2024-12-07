# Day 3: Mull It Over


from src import util

import re

data = util.input_single("day03.txt")


def star1():
    total = sum(
        int(m[0]) * int(m[1]) for m in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    )
    return total


def star2():
    total = 0

    on = True
    for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)", data):
        if m[0] == "don't()":
            on = False
        elif m[0] == "do()":
            on = True
        elif on:
            total += int(m[1]) * int(m[2])

    return total


util.run_day(3, star1, star2)
