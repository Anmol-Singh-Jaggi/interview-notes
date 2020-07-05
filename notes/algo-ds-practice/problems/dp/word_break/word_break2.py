"""
Same as word break but this time we have to print all the solutions.
"""
from functools import lru_cache
from collections import deque


words = None
line = None


@lru_cache(maxsize=None)
def word_break(i, j):
    global words
    global line
    if i > j:
        return [deque()]
    if i == j:
        if line[i] in words:
            dq = deque()
            dq.append((i, i))
            return [dq]
        return None
    ans = []
    for k in range(i, j + 1):
        sub1 = line[i : k + 1]
        if sub1 in words:
            sub_ans = word_break(k + 1, j)
            if sub_ans is not None:
                for dq in sub_ans:
                    dq_copy = deque(dq)
                    dq_copy.appendleft((i, k))
                    ans.append(dq_copy)
    return ans


def print_ans(dq_list):
    sentences = []
    global line
    for dq in dq_list:
        sentence = []
        for elem in dq:
            if len(elem) < 2:
                continue
            word = line[elem[0]: elem[1]+1]
            sentence.append(word)
        sentences.append(sentence)
    return sentences


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
    ans = print_ans(ans)
    print(ans)


main()
