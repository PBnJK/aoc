# Special: Intcode Interpreter


from typing import Callable


class IntCode:
    def __init__(self, program: list[int]) -> None:
        self.prg: list[int] = program.copy()
        self.mem: list[int] = []

        self.__run: bool = False
        self.__pc: int = 0

        self.__instr: dict[int, Callable] = {
            1: self.__construct_abc(self.__op_add_abc),  # M[C] = M[A] + M[B]
            2: self.__construct_abc(self.__op_mul_abc),  # M[C] = M[A] * M[B]
            99: self.__op_halt,  # HALT
        }

    def __op_add_abc(self, a: int, b: int, c: int) -> None:
        self.mem[c] = self.mem[a] + self.mem[b]

    def __op_mul_abc(self, a: int, b: int, c: int) -> None:
        self.mem[c] = self.mem[a] * self.mem[b]

    def __op_halt(self) -> None:
        self.__run = False

    def __construct_abc(self, fn: Callable[[int, int, int], None]) -> Callable:
        def c():
            a: int = self.__advance()
            b: int = self.__advance()
            c: int = self.__advance()
            fn(a, b, c)

        return c

    def __reset(self) -> None:
        self.mem = self.prg.copy()

        self.__run = True
        self.__pc = 0

    def __advance(self) -> int:
        op: int = self.mem[self.__pc]
        self.__pc += 1

        return op

    def insert(self, where: int, what: int) -> None:
        self.prg[where] = what

    def run(self) -> int:
        self.__reset()

        while self.__run:
            op: int = self.__advance()
            self.__instr[op]()

        return self.mem[0]
