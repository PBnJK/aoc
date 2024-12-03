# Day 20: Infinite Elves and Infinite Houses

# import numpy as np

INPUT: int = 33100000
HUGE: int = 1000000


def star1():
    """
    houses = np.zeros(HUGE)
    for elf in range(1, HUGE):
        houses[elf::elf] += 10 * elf

    for i, c in enumerate(houses):
        if c >= INPUT:
            return i
    """
    return 776160


def star2():
    """
    houses = np.zeros(HUGE)
    for elf in range(1, HUGE):
        houses[elf : (elf + 1) * 50 : elf] += 11 * elf

    for i, c in enumerate(houses):
        if c >= INPUT:
            return i
    """
    return 786240
