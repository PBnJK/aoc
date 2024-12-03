# Day 14: Reindeer Olympics


from src import util


class Reindeer:
    def __init__(self, name: str, speed: str, stime: str, rtime: str) -> None:
        self.name = name
        self.speed: int = int(speed)
        self.stime: int = int(stime)
        self.rtime: int = int(rtime)

        self.dist: int = 0
        self.points: int = 0

        self.ticker: int = self.stime
        self.resting: bool = False

    def reset(self) -> None:
        self.dist = 0
        self.points = 0

        self.ticker = self.stime
        self.resting = False

    def tick(self) -> None:
        if not self.resting:
            self.dist += self.speed

        self.ticker -= 1
        if self.ticker == 0:
            if self.resting:
                self.resting = False
                self.ticker = self.stime
            else:
                self.resting = True
                self.ticker = self.rtime


reindeer: list[Reindeer] = []
for r in util.input_lines("day14.txt"):
    name, _, _, speed, _, _, stime, _, _, _, _, _, _, rtime, _ = r.split()
    reindeer.append(Reindeer(name, speed, stime, rtime))


def star1():
    distances: list[int] = []
    for r in reindeer:
        for _ in range(2503):
            r.tick()

        distances.append(r.dist)

    return max(distances)


def star2():
    for r in reindeer:
        r.reset()

    for _ in range(2503):
        for r in reindeer:
            r.tick()

        dists: list[int] = [r.dist for r in reindeer]
        leader: int = max(dists)
        for r in reindeer:
            if r.dist == leader:
                r.points += 1

    return max([r.points for r in reindeer])
