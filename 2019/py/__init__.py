import src.day01 as day01
import src.day02 as day02

DAYS: list = [
    day01,
    day02,
]

for count, day in enumerate(DAYS, start=1):
    print(f"Day {count:02}:")
    print(f"  - STAR 1: {day.star1()}")
    print(f"  - STAR 2: {day.star2()}")
