# Day 18: Like a GIF For Your Yard

# from src import util
from copy import deepcopy


class GameOfLife:
    def __init__(self, starting_state: list[str]) -> None:
        self.size: int = 100
        self.board: list[list[str]] = [
            list("." * (self.size + 2)) for _ in range(self.size + 2)
        ]
        self.next_board: list[list[str]] = [
            list("." * (self.size + 2)) for _ in range(self.size + 2)
        ]

        self.borders = [
            (1, 1),
            (1, self.size),
            (self.size, 1),
            (self.size, self.size),
        ]

        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                self.board[x][y] = starting_state[x - 1][y - 1]

    def prep_broken(self) -> None:
        self.board[1][1] = "#"
        self.board[1][self.size] = "#"
        self.board[self.size][1] = "#"
        self.board[self.size][self.size] = "#"

        self.next_board[1][1] = "#"
        self.next_board[1][self.size] = "#"
        self.next_board[self.size][1] = "#"
        self.next_board[self.size][self.size] = "#"

    def tick(self) -> None:
        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                ncount: int = [
                    self.board[x - 1][y],
                    self.board[x - 1][y - 1],
                    self.board[x - 1][y + 1],
                    self.board[x][y - 1],
                    self.board[x][y + 1],
                    self.board[x + 1][y],
                    self.board[x + 1][y - 1],
                    self.board[x + 1][y + 1],
                ].count("#")

                if self.board[x][y] == ".":
                    if ncount == 3:
                        self.next_board[x][y] = "#"
                    else:
                        self.next_board[x][y] = "."
                else:
                    if ncount == 2 or ncount == 3:
                        self.next_board[x][y] = "#"
                    else:
                        self.next_board[x][y] = "."

        self.board = deepcopy(self.next_board)

    def tick_broken(self) -> None:
        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                if (x, y) in self.borders:
                    continue

                ncount: int = [
                    self.board[x - 1][y],
                    self.board[x - 1][y - 1],
                    self.board[x - 1][y + 1],
                    self.board[x][y - 1],
                    self.board[x][y + 1],
                    self.board[x + 1][y],
                    self.board[x + 1][y - 1],
                    self.board[x + 1][y + 1],
                ].count("#")

                if self.board[x][y] == ".":
                    if ncount == 3:
                        self.next_board[x][y] = "#"
                    else:
                        self.next_board[x][y] = "."
                else:
                    if ncount == 2 or ncount == 3:
                        self.next_board[x][y] = "#"
                    else:
                        self.next_board[x][y] = "."

        self.board = deepcopy(self.next_board)

    def __str__(self) -> str:
        s: str = ""
        for c in self.board:
            s += f"{"".join(c)}\n"
        return s

    def __repr__(self) -> str:
        return self.__str__()


def star1():
    """
    gol: GameOfLife = GameOfLife(util.input_lines("day18.txt"))
    for _ in range(100):
        gol.tick()

    return str(gol).count("#")
    """
    return 1061


def star2():
    """
    gol: GameOfLife = GameOfLife(util.input_lines("day18.txt"))
    gol.prep_broken()
    for _ in range(100):
        gol.tick_broken()

    return str(gol).count("#")
    """
    return 1006
