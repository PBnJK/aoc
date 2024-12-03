# Day 02: I Was Told There Would Be No Math


from src import util


def get_dims() -> list[tuple[int, int, int]]:
    dims: list[tuple[int, int, int]] = []

    inp: list[str] = util.input_lines("day02.txt")
    for box in inp:
        length, width, heigth = box.split("x")
        dims.append((int(length), int(width), int(heigth)))

    return dims


def star1():
    dims = get_dims()

    sq = 0
    for l, w, h in dims:
        sa = l * w
        sb = w * h
        sc = h * l

        sq += 2 * sa + 2 * sb + 2 * sc + min([sa, sb, sc])

    return sq


def star2():
    dims = get_dims()

    ribbon = 0
    for d in dims:
        sort = sorted(d)
        ribbon += sort[0] * 2 + sort[1] * 2
        ribbon += d[0] * d[1] * d[2]

    return ribbon
