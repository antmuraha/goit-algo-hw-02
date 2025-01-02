from collections import deque
import re


def palindrome_check(word: str):
    d = deque()
    word = re.sub(r"[\s\.\,\']", "", word.lower())
    for ch in word:
        d.append(ch)

    while len(d):
        length = len(d)
        if length < 2:
            return True

        first = d.popleft()
        last = d.pop()
        if first != last:
            return False

    return True
