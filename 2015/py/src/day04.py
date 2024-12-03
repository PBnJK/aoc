# Day 04: The Ideal Stocking Stuffer

# This one takes a while, so we cache the results
# Uncomment the import below + the code inside the functions to run it
# import hashlib

INPUT: str = "yzbqklnj"


def star1():
    """
    for i in range(10000000):
        hash = hashlib.md5(f"{INPUT}{i}".encode()).hexdigest()
        if hash[:5] == "00000":
            return i
    """
    return 282749


def star2():
    """
    for i in range(10000000):
        hash = hashlib.md5(f"{INPUT}{i}".encode()).hexdigest()
        if hash[:6] == "000000":
            return i
        pass
    """
    return 9962624
