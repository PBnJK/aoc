# Day 4: Ceres Search

from src import util

SIZE = 146
EMPTY = "." * SIZE
PAD = "." * 3

path = util.get_input_path("day04.txt")
with open(path, "r") as f:
    ws = [EMPTY, EMPTY, EMPTY]
    for line in f.readlines():
        ws.append(PAD + line.strip() + PAD)

ws.append(EMPTY)
ws.append(EMPTY)
ws.append(EMPTY)


def checkhorz(line, i):
    matches = 0
    if line[i + 1 : i + 4] == "MAS":
        matches += 1
    if line[i - 1 : i - 4 : -1] == "MAS":
        matches += 1

    return matches


def checkvert(li, i):
    matches = 0
    if ws[li + 1][i] == "M" and ws[li + 2][i] == "A" and ws[li + 3][i] == "S":
        matches += 1
    if ws[li - 1][i] == "M" and ws[li - 2][i] == "A" and ws[li - 3][i] == "S":
        matches += 1

    return matches


def checkdiag(li, i):
    matches = 0
    if (
        ws[li + 1][i + 1] == "M"
        and ws[li + 2][i + 2] == "A"
        and ws[li + 3][i + 3] == "S"
    ):
        matches += 1
    if (
        ws[li - 1][i + 1] == "M"
        and ws[li - 2][i + 2] == "A"
        and ws[li - 3][i + 3] == "S"
    ):
        matches += 1
    if (
        ws[li + 1][i - 1] == "M"
        and ws[li + 2][i - 2] == "A"
        and ws[li + 3][i - 3] == "S"
    ):
        matches += 1
    if (
        ws[li - 1][i - 1] == "M"
        and ws[li - 2][i - 2] == "A"
        and ws[li - 3][i - 3] == "S"
    ):
        matches += 1

    return matches


def star1():
    total = 0
    for lidx, line in enumerate(ws):
        for cidx, c in enumerate(line):
            if c != "X":
                continue

            total += checkhorz(line, cidx)
            total += checkvert(lidx, cidx)
            total += checkdiag(lidx, cidx)

    return total


def checkmas(l1, l2, l3):
    return int(
        l2[1] == "A"
        and ((l1[0] == "M" and l3[2] == "S") or (l1[0] == "S" and l3[2] == "M"))
        and ((l1[2] == "M" and l3[0] == "S") or (l1[2] == "S" and l3[0] == "M"))
    )


def star2():
    total = 0
    for i in range(3, 141):
        for j in range(3, 141):
            total += checkmas(
                ws[i][j : j + 3], ws[i + 1][j : j + 3], ws[i + 2][j : j + 3]
            )

    return total
