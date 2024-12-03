# Day 15: Science for Hungry People


class Ingredient:
    def __init__(self, cap: int, d: int, f: int, t: int, cal: int) -> None:
        self.capacity: int = cap
        self.durability: int = d
        self.flavor: int = f
        self.texture: int = t
        self.calories: int = cal

    def get_amounts(self, tsp: int) -> tuple[int, int, int, int]:
        return (
            self.capacity * tsp,
            self.durability * tsp,
            self.flavor * tsp,
            self.texture * tsp,
        )

    def get_calories(self, tsp: int) -> int:
        return self.calories * tsp


ingredients: list[Ingredient] = [
    Ingredient(3, 0, 0, -3, 2),
    Ingredient(-3, 3, 0, 0, 9),
    Ingredient(-1, 0, 4, 0, 1),
    Ingredient(0, 0, -2, 2, 8),
]


def star1():
    """
    best: list[int] = []
    for i in range(0, 100):
        for j in range(0, 100 - i):
            for k in range(0, 100 - i - j):
                l = 100 - i - j - k
                props = [
                    sum(q)
                    for q in zip(
                        ingredients[0].get_amounts(i),
                        ingredients[1].get_amounts(j),
                        ingredients[2].get_amounts(k),
                        ingredients[3].get_amounts(l),
                    )
                ]

                if any(q <= 0 for q in props):
                    continue

                best.append(props[0] * props[1] * props[2] * props[3])

    return max(best)
    """
    return 222870


def star2():
    """
    best: list[int] = []
    for i in range(0, 100):
        for j in range(0, 100 - i):
            for k in range(0, 100 - i - j):
                l = 100 - i - j - k
                props = [
                    sum(q)
                    for q in zip(
                        ingredients[0].get_amounts(i),
                        ingredients[1].get_amounts(j),
                        ingredients[2].get_amounts(k),
                        ingredients[3].get_amounts(l),
                    )
                ]

                if (
                    sum([x.get_calories(y) for x, y in zip(ingredients, (i, j, k, l))])
                    != 500
                ):
                    continue

                if any(q <= 0 for q in props):
                    continue

                best.append(props[0] * props[1] * props[2] * props[3])

    return max(best)
    """
    return 117936
