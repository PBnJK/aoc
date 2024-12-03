# Day 05: Doesn't He Have Intern-Elves For This?

from src import util


def star1():
    nice: int = 0

    words: list[str] = util.input_lines("day05.txt")
    for word in words:
        # Vowel check
        if sum([word.count(x) for x in "aeiou"]) < 3:
            continue

        # Doubles check
        for e, c in enumerate(word, start=0):
            if e < len(word) - 1 and c == word[e + 1]:
                break
        else:
            continue

        # Naughty pairs check
        if any([p in word for p in ["ab", "cd", "pq", "xy"]]):
            continue

        nice += 1

    return nice


def star2():
    nice: int = 0

    words: list[str] = util.input_lines("day05.txt")
    for word in words:
        bigrams: list[str] = ["".join(pair) for pair in zip(word, word[1:])]
        if not any(word.count(bigram) > 1 for bigram in bigrams):
            continue

        trigrams: list[str] = ["".join(trio) for trio in zip(word, word[1:], word[2:])]
        if not any(trigram[0] == trigram[2] for trigram in trigrams):
            continue

        nice += 1

    return nice
