# Day 5: Print Queue

from src import util

rules, pages = util.input_single("day05.txt").split("\n\n")

rules = rules.split("\n")
pages = pages.split("\n")


def star1():
    rule = {}
    for r in rules:
        f, t = r.split("|")

        if f in rule:
            rule[f].add(t)
        else:
            rule[f] = {t}

    valid = []
    for page in pages:
        visited = set()
        good = True
        page = page.split(",")

        for p in page:
            if (p in rule) and not rule[p].isdisjoint(visited):
                good = False
                break

            visited.add(p)

        if good:
            valid.append(page)

    return sum(int(x[(len(x) - 1) // 2]) for x in valid)


def star2():
    rule = {}
    for r in rules:
        f, t = r.split("|")

        if f in rule:
            rule[f].add(t)
        else:
            rule[f] = {t}

    invalid = []
    for page in pages:
        visited = set()
        bad = False
        page = page.split(",")

        for p in page:
            if (p in rule) and not rule[p].isdisjoint(visited):
                bad = True
                break

            visited.add(p)

        if bad:
            invalid.append(page)

    for v in invalid:
        swaps = 0
        while True:
            for i in range(len(v) - 1):
                if (v[i + 1] in rule) and v[i] in rule[v[i + 1]]:
                    v[i], v[i + 1] = v[i + 1], v[i]
                    swaps += 1

            if swaps == 0:
                break

            swaps = 0

    return sum(int(x[(len(x) - 1) // 2]) for x in invalid)


util.run_day(5, star1, star2)
