'''
Same as interval scheduling, but this time every event has some weight/importance, and we need to maximize the total output importance, rather than the number of events.
See algo on <https://kartikkukreja.wordpress.com/2013/10/06/weighted-interval-scheduling-problem/>.
Warning: WA on https://www.spoj.com/problems/RENT
'''
import operator
from bisect import bisect


def interval_scheduling_weighted(activities):
    """
    See notes for algo description.
    """
    # Sort by (finishing time, weight, starting time).
    activities = sorted(activities, key=operator.itemgetter(1, 2, 0))
    # Separate out the array into 2; one for start_time, one for end_time.
    activities_st, activities_et, _ = zip(*activities)
    activities_et = list(activities_et)
    activities_st = list(activities_st)
    # Compute prev_compatible, also called `p[j]`...
    prev_compatible_idx = [-1] * len(activities)
    for i in range(len(activities)):
        activity_st = activities_st[i]
        # Find the latest event whose et <= st and et of this event.
        # That is, the latest event among all the previous events
        # that does not clash with this event.
        compatible_activity_idx = bisect(activities_et, activity_st, 0, i) - 1
        if (
            compatible_activity_idx >= 0
            and activities_et[compatible_activity_idx] <= activity_st
        ):
            prev_compatible_idx[i] = compatible_activity_idx
    dp = [0] * len(activities)
    dp[0] = activities[0][2]
    for i in range(1, len(activities)):
        # The answer already computed for the latest previous compatible event.
        prev_compatible_answer = 0
        if prev_compatible_idx[i] >= 0:
            prev_compatible_answer = dp[prev_compatible_idx[i]]
        dp[i] = max(activities[i][2] + prev_compatible_answer, dp[i - 1])
    return dp[len(dp) - 1]


def main():
    activities = [(1, 2, 1), (3, 4, 10), (0, 6, 4), (5, 7, 2), (8, 9, 0), (5, 9, 15)]
    print(interval_scheduling_weighted(activities))


if __name__ == "__main__":
    main()
