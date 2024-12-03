# Day 21: RPG Simulator 20XX

from itertools import product, combinations


IDX_COST: int = 0
IDX_ATK: int = 1
IDX_DEF: int = 2


class Stats:
    def __init__(self, attack: int, defense: int, items=None) -> None:
        self.attack: int = attack
        self.defense: int = defense

        self.cost: int = 0

        if items:
            self.cost += items[0][IDX_COST]
            self.cost += items[1][IDX_COST]
            self.cost += items[2][0][IDX_COST]
            self.cost += items[2][1][IDX_COST]

            self.attack += items[0][IDX_ATK]
            self.attack += items[1][IDX_ATK]
            self.attack += items[2][0][IDX_ATK]
            self.attack += items[2][1][IDX_ATK]

            self.defense += items[0][IDX_DEF]
            self.defense += items[1][IDX_DEF]
            self.defense += items[2][0][IDX_DEF]
            self.defense += items[2][1][IDX_DEF]


class Character:
    def __init__(self, health: int, stats: Stats) -> None:
        self.health: int = health
        self.stats: Stats = stats

    def tick(self, enemy) -> bool:
        return enemy.hurt(self.stats.attack)

    def hurt(self, damage: int) -> bool:
        self.health -= max(1, damage - self.stats.defense)
        return self.health <= 0


weapons: list[tuple[int, int, int]] = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]

armor: list[tuple[int, int, int]] = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
]

rings: list[tuple[int, int, int]] = [
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]


def star1():
    items = product(weapons, armor, combinations(rings, 2))
    costs: set[int] = set()

    for item in items:
        player: Character = Character(100, Stats(0, 0, item))
        enemy: Character = Character(104, Stats(8, 1))

        while True:
            if player.tick(enemy):
                costs.add(player.stats.cost)
                break

            if enemy.tick(player):
                break

    return min(costs)


def star2():
    items = product(weapons, armor, combinations(rings, 2))
    costs: set[int] = set()

    for item in items:
        player: Character = Character(100, Stats(0, 0, item))
        enemy: Character = Character(104, Stats(8, 1))

        while True:
            if player.tick(enemy):
                break

            if enemy.tick(player):
                costs.add(player.stats.cost)
                break

    return max(costs)
