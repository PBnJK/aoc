# Day 10: Elves Look, Elves Sa

# This one takes a little bit, so we cache it too
# You know the drill; uncomment to run!

"""
INPUT: str = "1113122113"

def lns(times: int) -> int:
    seq: str = INPUT
    for _ in range(times):
        pc: str = seq[0]
        cc: int = 0

        nseq: str = ""

        for c in seq:
            if c != pc:
                nseq += f"{cc}{pc}"
                pc = c
                cc = 1
                continue

            cc += 1

        nseq += f"{cc}{pc}"

        seq = nseq

    return len(seq)
"""


def star1():
    # return lns(40)
    return 360154


def star2():
    # return lns(50)
    return 5103798
