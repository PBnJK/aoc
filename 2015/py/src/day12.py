# Day 12: JSAbacusFramework.io


import builtins
import json
from src import util
# from json import j


def star1():
    js: str = util.input_single("day12.txt")
    ns: str = "-1234567890"

    total: int = 0
    i: int = 0
    while i < len(js):
        num: str = ""
        if js[i] not in ns:
            i += 1
            continue

        while js[i] in ns:
            num += js[i]
            i += 1

        total += int(num)

    return total


def traverse(p) -> int:
    match type(p):
        case builtins.int:
            return p
        case builtins.dict:
            if "red" in p.keys() or "red" in p.values():
                return 0
            return sum(traverse(p[child]) for child in p)
        case builtins.list:
            return sum(traverse(child) for child in p)

    return 0


def star2():
    js: str = util.input_single("day12.txt")
    return traverse(json.loads(js))
