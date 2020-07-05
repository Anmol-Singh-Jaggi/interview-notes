"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


def merge_intervals(intervals):
    if not intervals:
        return intervals
    intervals.sort()
    intervals_new = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][1] <= intervals_new[-1][1]:
            pass
        elif intervals[i][0] <= intervals_new[-1][1]:
            intervals_new[-1][1] = intervals[i][1]
        else:
            intervals_new.append(intervals[i])
    return intervals_new


def main():
    intervals = []
    intervals.append([1, 3])
    intervals.append([2, 6])
    intervals.append([8, 10])
    intervals.append([15, 18])
    intervals.append([15, 19])
    ans = merge_intervals(intervals)
    print(ans)


main()
