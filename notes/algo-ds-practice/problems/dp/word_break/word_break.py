from functools import lru_cache

words = None
line = None


@lru_cache(maxsize=None)
def word_break(i, j):
    global words
    global line
    if i > j:
        return True
    if i == j:
        if line[i] in words:
            return True
        return False
    for k in range(i, j + 1):
        sub1 = line[i: k + 1]
        if sub1 in words and word_break(k + 1, j):
            return True
    return None


def main():
    global words
    global line
    line = "ilikesamsung"
    words = [
        "i",
        "like",
        "sam",
        "sung",
        "samsung",
        "mobile",
        "ice",
        "cream",
        "icecream",
        "man",
        "go",
        "mango",
    ]
    words = set(words)
    ans = word_break(0, len(line) - 1)
    print(ans)


main()
