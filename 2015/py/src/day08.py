# Day 08: Matchsticks


from src import util


def star1():
    total: int = 0
    for s in util.input_lines("day08.txt"):
        str_code: int = len(s)

        str_value: int = 0
        c: int = 1
        while c < str_code - 1:
            if s[c] == "\\":
                c += 1
                match s[c]:
                    case "\\":
                        str_value += 1
                    case '"':
                        str_value += 1
                    case "x":
                        c += 2
                        str_value += 1
            else:
                str_value += 1

            c += 1

        total += str_code - str_value

    return total


def star2():
    total: int = 0
    for s in util.input_lines("day08.txt"):
        str_code: int = len(s)

        string: str = ""
        c: int = 0
        while c < str_code:
            match s[c]:
                case '"':
                    string += '\\"'
                case "\\":
                    string += "\\\\"
                    match s[c + 1]:
                        case "\\":
                            string += "\\\\"
                            c += 1
                        case '"':
                            string += '\\"'
                            c += 1
                case char:
                    string += char

            c += 1

        string = '"' + string + '"'
        total += len(string) - str_code

    return total
