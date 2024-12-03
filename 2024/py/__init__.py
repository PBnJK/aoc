import src.day01 as day01
import src.day02 as day02
import src.day03 as day03

DAYS: list = [
    day01,
    day02,
    day03,
]

for count, day in enumerate(DAYS, start=1):
    print(f"Day {count:02}:")
    print(f"  - STAR 1: {day.star1()}")
    print(f"  - STAR 2: {day.star2()}")
