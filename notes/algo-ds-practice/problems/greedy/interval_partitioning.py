'''
Given a set `{1, 2, …, n}` of `n` requests/events, where `ith` request starts at time `s(i)` and finishes at time `f(i)`, find the minimum number of resources needed to schedule all requests so that no two requests are assigned to the same resource at the same time. Two requests `i` and `j` can conflict in one of two ways:

    s(i) <= s(j) and f(i) > s(j)
    s(j) <= s(i) and f(j) > s(i)

Example:
Given 3 requests with:
s(1) = 1, f(1) = 3
s(2) = 2, f(2) = 4
s(3) = 3, f(3) = 5

At least 2 resources are needed to satisfy all requests.


**Alternate statement**

Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required for the railway station so that no train waits.
We are given two arrays which represent arrival and departure times of trains that stop.

Examples:

Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
        dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
There are at-most three trains at a time (time between 11:00 to 11:20)


**Yet another alternate statement**

Lecture i starts at `s[i]` and finishes at `f[i]`.
Goal: Find minimum number of classrooms to schedule all lectures so that no two occur at the same time in the same room.


SOLUTIONS:

SOLUTION 1:
This problem can be solved optimally with a greedy strategy of scheduling requests based on earliest start time i.e., from the set of remaining requests, we always select the one with the earliest start time and assign it to one of the available resources (if it would not cause a conflict) or demand another resource for this request.
Complexity -> O(nlogn)

SOLUTION 2:
Lets say the max ending time of any interval is 'x'.
Then we can create an array of size x + 1 initialized with 0.
Then we can iterate through the intervals.
For every interval (start, end), we can do arr[start]++ and arr[end]--.
At the end, start iterating the array from index 1 and keep a cumulative sum 'cumsum'
The answer would be the max of any of the cumsums.
for i in range(1, x + 1){
    cumsum += arr[i]
    ans = max(ans, cumsum)
}

SOURCE: https://leetcode.com/problems/car-pooling/discuss/390356/Most-simple-solution-O(n)-(10-lines)-with-explanation-(without-sorting-without-map-without-tree!)

'''


def interval_partitioning(events):
    """
    Created a sorted collection of `Event(t)`, where an event can be arrival or
    departure, sorted based on the time.
    Then starting from the beginning, keep a count of `#arrival - #departure`.
    The max value ever encountered of `#arrival - #departure` is the answer.
    """
    # CAREFUL: I was thinking of heap, but this solution is so much better than that.
    events_sorted = []
    for event in events:
        events_sorted.append((event[0], True))
        events_sorted.append((event[1], False))
    events_sorted.sort()
    answer = 0
    num_resources_required_right_now = 0
    for event in events_sorted:
        if event[1]:
            num_resources_required_right_now += 1
        else:
            num_resources_required_right_now -= 1
        answer = max(answer, num_resources_required_right_now)
    return answer


def main():
    activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
    print(interval_partitioning(activities))


if __name__ == "__main__":
    main()
