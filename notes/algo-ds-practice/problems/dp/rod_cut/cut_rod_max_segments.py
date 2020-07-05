"""
Given an integer 'length' denoting the length of a line segment.
You need to cut the line segment in such a way that the cut length of
a line segment is among the set of numbers 'segments'
and the total number of cutted segments must be **maximum**.

Input

2
4
2 1 1
5
5 3 2


Output
4
2

In first test case, total length is 4, and cut lengths are 2, 1 and 1.
We can make maximum 4 segments each of length 1.
In second test case, we can make two segments of lengths 3 and 2.

SOLUTION:

Almost similar to the coin-change-min problem; just replace min() with max().
"""


def get_max_segments(length, segments, cache):
    if length == 0:
        cache[0] = (0, {})
    if length in cache:
        return cache[length]
    ans = None
    answer_mapping = {}
    for i in range(len(segments)):
        seg = segments[i]
        if length >= seg:
            sub_ans, sub_ans_mapping = get_max_segments(length - seg, segments, cache)
            if sub_ans is None:
                continue
            if ans is None:
                ans = 0
            sub_ans += 1
            if sub_ans > ans:
                ans = sub_ans
                answer_mapping = dict(sub_ans_mapping)
                answer_mapping[seg] = answer_mapping.get(seg, 0) + 1
    cache[length] = (ans, answer_mapping)
    return ans, answer_mapping


def main():
    length = 5
    segments = [2, 3, 5]
    ans = get_max_segments(length, segments, {})
    print(ans)


main()

