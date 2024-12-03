# Day 19: Medicine for Rudolph

import re

from src import util

# Alright, confession time (again; see day 9)
#
# IN MY DEFENSE: Look at this crap:
# https://old.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju/
#
# You could--and I'm only half joking here--write a whole damn paper with this!
#
# In all seriousness, it's a tough problem, and the solution found by
# u/askalski is incredibly clever. I won't write another diatribe, but I have
# commented the star2 function (because the star1 function was all me :D) to
# try and explain what's going on.


def star1():
    substs: dict[str, list[str]] = {}
    instr: list[str] = util.input_lines("day19.txt")
    for pair in instr:
        if not pair:
            break

        left, right = pair.split("=>")
        substs.setdefault(left.strip(), []).append(right.strip())

    base: str = instr[-1]
    molecules: set[str] = set()
    for pattern in substs:
        for repl in substs[pattern]:
            for m in re.finditer(pattern, base):
                c = base[: m.start()] + repl + base[m.end() :]
                molecules.add(c)

    return len(molecules)


def star2():
    subst: dict[str, str] = {}
    instr: list[str] = util.input_lines("day19.txt")
    for pair in instr:
        if not pair:
            break

        left, right = pair.split("=>")

        # Alright. As opposed to star1, we're not doing a dict of lists
        #
        # Instead, by looking at the input for more than two seconds, one can
        # see that the *right* molecule is a unique identifier.
        #
        # As such, we store the substitutions inversed (which is also helpful
        # later!)
        #
        # Also, note the [::-1]. That inverses the string. Why? Well, I'm gonna
        # be honest with ya, you gotta read u/askalski's comment for that.
        #
        # The short version is that, if you stare at the input again, you'll
        # notice lots of weird little "Rn"s and "Y"s and "Ar"s. Those, funnily
        # enough, form a neat pattern.
        #
        # As consequence of that pattern, however, matching from the left can
        # back us into a corner, since the "Ar"s always (when they appear)
        # close an expression. Reversing the strings causes us to get rid of
        # the "Ar"s early, avoiding getting trapped.
        #
        # ...
        #
        # ...I only half-understood that.
        subst[right.strip()[::-1]] = left.strip()[::-1]

    # This pattern matches any molecules we are aware of
    # Mg OR Au OR TiTiCaCa OR ...
    PATTERN: str = "|".join(subst.keys())

    base: str = instr[-1][::-1]
    count: int = 0
    # OK. What's this?
    #
    # Well to solve this problem, we're gonna have to work backwards.
    # Instead of starting at an electron and working towards a molecule, we
    # start from the finished molecule and work backwards until we end up back
    # at the starting point (the electron!)
    while base != "e":
        # Let's go step-by-step:
        #
        # 1. PATTERN: This matches any molecule we know of. re.sub finds the
        #             first match from the right, so it gets the first molecule
        #             it can find there. Since we reversed the base, we are
        #             actually marching *backwards* through the string.
        #
        # 2. lambda: This is cool; re.sub let's us pass a function as the 2nd
        #            argument. Normally, that's the string that will replace
        #            whatever match it finds, but when we pass a function, it
        #            will instead call that function and expect its return
        #            value to serve as the replacement string.
        #
        #            It's pretty obvious what we are doing then: It calls the
        #            lambda, which returns the proper substitution from the
        #            dict we made earlier
        #
        # 3. base: String that we are searching for matches in.
        #          Self-explanatory.
        #
        # 4. 1: This informs re.sub to substitute only 1 time. Also pretty
        #       self-explanatory.
        base = re.sub(PATTERN, lambda m: subst[m.group()], base, 1)
        count += 1

    return count
