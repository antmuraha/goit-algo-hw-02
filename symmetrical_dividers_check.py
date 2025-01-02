import re

COUPLES = {
    "]": "[",
    "}": "{",
    ")": "(",
}


def symmetrical_dividers_check(line: str):
    d = []
    line = re.sub(r"[^\{\}\(\)\[\]]", "", line)

    if len(line) % 2:
        return False

    for ch in line:
        length = len(d)
        if length:
            last = d[length - 1]
            if last == COUPLES.get(ch):
                d.pop()
            else:
                d.append(ch)
        else:
            d.append(ch)

    return len(d) == 0
