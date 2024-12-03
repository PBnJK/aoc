# Day 07: Some Assembly Required

from src import util

circuit: dict[str, list[str]] = {}
output: dict[str, int] = {}

instructions: list[str] = util.input_lines("day07.txt")
for i in instructions:
    lhs, rhs = i.split("->")
    rhs = rhs.strip()
    circuit[rhs] = lhs.split()


def solve(wire: str) -> int:
    if wire not in output:
        if wire.isnumeric():
            value = int(wire)
        else:
            i = circuit[wire]
            if len(i) == 1:
                value = solve(i[0])
            else:
                match i[1]:
                    case "LSHIFT":
                        value = solve(i[0]) << solve(i[2])
                    case "RSHIFT":
                        value = solve(i[0]) >> solve(i[2])
                    case "AND":
                        value = solve(i[0]) & solve(i[2])
                    case "OR":
                        value = solve(i[0]) | solve(i[2])
                    case _:
                        value = ~solve(i[1])

        output[wire] = value

    return output[wire]


def star1():
    return solve("a")


def star2():
    global output
    circuit["b"] = [str(output["a"])]

    output = {}
    return solve("a")
