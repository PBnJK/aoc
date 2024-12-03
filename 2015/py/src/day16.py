# Day 16: Aunt Sue

import re

from src import util

PATTERN: str = r"Sue \d+: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)"

sues: list[dict[str, int]] = []
for sue in util.input_lines("day16.txt"):
    m: re.Match = re.findall(PATTERN, sue)[0]
    sues.append(
        {
            m[0]: int(m[1]),
            m[2]: int(m[3]),
            m[4]: int(m[5]),
        }
    )

target: dict[str, int] = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def star1():
    for i, sue in enumerate(sues):
        for k in sue:
            if sue[k] != target[k]:
                break
        else:
            return i + 1

    return "OOPS"


def star2():
    for i, sue in enumerate(sues):
        for k in sue:
            match k:
                case "cats" | "trees":
                    if sue[k] <= target[k]:
                        break
                case "pomeranians" | "goldfish":
                    if sue[k] >= target[k]:
                        break
                case _:
                    if sue[k] != target[k]:
                        break
        else:
            return i + 1

    return "OOPS"
