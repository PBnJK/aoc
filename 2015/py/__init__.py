import src.day01 as day01
import src.day02 as day02
import src.day03 as day03
import src.day04 as day04
import src.day05 as day05
import src.day06 as day06
import src.day07 as day07
import src.day08 as day08
import src.day09 as day09
import src.day10 as day10
import src.day11 as day11
import src.day12 as day12
import src.day13 as day13
import src.day14 as day14
import src.day15 as day15
import src.day16 as day16
import src.day17 as day17
import src.day18 as day18
import src.day19 as day19
import src.day20 as day20
import src.day21 as day21
import src.day22 as day22
import src.day23 as day23
import src.day24 as day24
import src.day25 as day25

days = [
    day01,
    day02,
    day03,
    day04,
    day05,
    day06,
    day07,
    day08,
    day09,
    day10,
    day11,
    day12,
    day13,
    day14,
    day15,
    day16,
    day17,
    day18,
    day19,
    day20,
    day21,
    day22,
    day23,
    day24,
    day25,
]

for day in days:
    print(f"{day.__name__[4:]}:")
    print(f"STAR 1: {day.star1()}")
    print(f"STAR 2: {day.star2()}\n")
