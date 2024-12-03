# Day 06: Probably A Fire Hazard


# This one is also pretty slow, so we cache it too
# Uncomment the import below, the coords function and the code in the star
# functions to run it
# from src import util

"""
def coords(c) -> tuple[int, int]:
    x, y = c.split(",")
    return int(x), int(y)
"""


def star1():
    """
    lights: list[bool] = [False for _ in range(1000 * 1000)]
    instructions: list[str] = util.input_lines("day06.txt")
    for ins in instructions:
        s = ins.split()
        if s[0] == "toggle":
            typ, start, end = "toggle", s[1], s[3]
        else:
            typ, start, end = " ".join(s[:2]), s[2], s[4]

        sc, ec = coords(start), coords(end)

        if typ == "toggle":
            for x in range(sc[0], ec[0] + 1):
                for y in range(sc[1], ec[1] + 1):
                    lights[x + y * 1000] = not lights[x + y * 1000]
        elif typ == "turn on":
            for x in range(sc[0], ec[0] + 1):
                for y in range(sc[1], ec[1] + 1):
                    lights[x + y * 1000] = True
        elif typ == "turn off":
            for x in range(sc[0], ec[0] + 1):
                for y in range(sc[1], ec[1] + 1):
                    lights[x + y * 1000] = False

    return lights.count(True)
    """
    return 569999


def star2():
    """
    lights: list[int] = [0 for _ in range(1000 * 1000)]
    instructions: list[str] = util.input_lines("day06.txt")
    for ins in instructions:
        s = ins.split()
        if s[0] == "toggle":
            typ, start, end = "toggle", s[1], s[3]
        else:
            typ, start, end = " ".join(s[:2]), s[2], s[4]

        sc, ec = coords(start), coords(end)

        if typ == "toggle":
            for x in range(sc[0], ec[0] + 1):
                for y in range(sc[1], ec[1] + 1):
                    lights[x + y * 1000] += 2
        elif typ == "turn on":
            for x in range(sc[0], ec[0] + 1):
                for y in range(sc[1], ec[1] + 1):
                    lights[x + y * 1000] += 1
        elif typ == "turn off":
            for x in range(sc[0], ec[0] + 1):
                for y in range(sc[1], ec[1] + 1):
                    if lights[x + y * 1000] > 0:
                        lights[x + y * 1000] -= 1

    return sum(lights)
    """
    return 17836115
