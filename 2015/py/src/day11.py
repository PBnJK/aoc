# Day 11: Corporate Policy

#  hey
#     guess
# what
#     this
#  one
#     is
# slow
#     so
#   we
#     cache
#   it

INPUT = "vzbxkghb"


class NumPwd:
    def __init__(self, pwd: str) -> None:
        self.npwd: list[int] = [ord(c) - ord("a") for c in pwd]

        self.illegal = [ord("i") - ord("a"), ord("o") - ord("a"), ord("l") - ord("a")]

    def is_valid(self) -> bool:
        # Illegal characters check
        if any([c in self.npwd for c in self.illegal]):
            return False

        # Increasing straight check
        trigrams: list[tuple[int, int, int]] = [
            trio for trio in zip(self.npwd, self.npwd[1:], self.npwd[2:])
        ]
        if not any([t[0] == t[1] - 1 == t[2] - 2 for t in trigrams]):
            return False

        # Double doubles check
        bigrams: list[tuple[int, int]] = [
            pair for pair in zip(self.npwd, self.npwd[1:])
        ]
        doubles: list[int] = []
        for p in bigrams:
            if p[0] == p[1] and p[0] not in doubles:
                if len(doubles) == 1:
                    break

                doubles.append(p[0])
        else:
            return False

        return True

    def increment(self) -> None:
        at: int = -1
        while True:
            self.npwd[at] += 1
            if self.npwd[at] < 26:
                if not self.is_valid():
                    continue
                break

            while True:
                self.npwd[at] = 0
                at -= 1
                self.npwd[at] += 1
                if self.npwd[at] < 26:
                    at = -1
                    self.npwd[at] = -1
                    break

    def __str__(self) -> str:
        return "".join([chr(i + ord("a")) for i in self.npwd])

    def __repr__(self) -> str:
        return self.__str__()


def star1():
    """
    npwd = NumPwd(INPUT)
    npwd.increment()

    return str(npwd)
    """
    return "vzbxxyzz"


def star2():
    """
    npwd = NumPwd(star1())
    npwd.increment()

    return str(npwd)
    """
    return "vzcaabcc"
