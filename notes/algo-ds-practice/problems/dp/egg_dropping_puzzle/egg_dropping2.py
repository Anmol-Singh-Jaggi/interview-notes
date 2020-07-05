from functools import lru_cache


@lru_cache(maxsize=None)
def compute_ncr(n, r):
    if n == r:
        return 1
    if n == 0:
        return 0
    if r == 0:
        return 1
    return compute_ncr(n - 1, r - 1) + compute_ncr(n - 1, r)


@lru_cache(maxsize=None)
def get_num_floors_max(num_eggs, num_trials):
    '''
    Max floors that can be evaluated as breaking or non-breaking
    using 'num_trials' egg drops.
    summation[ C(num_trials, x) ] for x = 1 ... min(num_trials, num_eggs)

    Proof:
    Let X = ans(eggs-1, trials-1); for when egg breaks.
    Let Y = ans(eggs, trials-1); for when egg doesn't break.
    X and Y denote the number of max floors that can be evaluated
    in downwards and upwards direction respectively.

    Now, if we start our first trial at floor number X+1, then
    either egg breaks, in which case we have evaluated floor X+1 and above,
    and use (trials-1) more trials to evaluate X floors below (by definition of X),
    thus covering all the floors.
    Or the egg does not break, which means we have evaluated floor X+1 and below,
    and use (trials-1) more trials for the Y floors above (by definition of Y),
    thus covering (X+1)+Y floors.

    Since, we want the worst case scenario, we'll go with the second case.
    Which means:
    ans(egg, trials) = ans(eggs-1, trials-1) + ans(eggs, trials-1) + 1

    See these for more info:
    https://brilliant.org/wiki/egg-dropping/
    https://www.youtube.com/watch?v=xsOCvSiSrSs
    '''
    ans = 0
    for i in range(1, min(num_eggs + 1, num_trials + 1)):
        ans += compute_ncr(num_trials, i)
    return ans


@lru_cache(maxsize=None)
def get_min_trials(num_eggs, num_floors):
    '''
    Start from num_trials = 1 .. num_floors one-by-one and check if
    the number of floors covered by num_trials is >= num_floors.
    Return first such 'num_trials';
    Complexity -> O(nk)
    '''
    for num_trials in range(1, num_floors + 1):
        num_floors_max = get_num_floors_max(num_eggs, num_trials)
        if num_floors_max >= num_floors:
            return num_trials


@lru_cache(maxsize=None)
def get_min_trials_binary_search(num_eggs, num_floors):
    '''
    Instead of linear search, do a binary search for 'num_trials'
    from 1 to num_floors.
    Complexity -> O(nlogk), where n = num_eggs.
    '''
    low = 1
    high = num_floors
    while low < high:
        num_trials = (low + high) // 2
        num_floors_max = get_num_floors_max(num_eggs, num_trials)
        if num_floors_max < num_floors:
            low = num_trials + 1
        else:
            high = num_trials
    return low


def main():
    num_eggs = 2
    num_floors = 100
    ans = get_min_trials_binary_search(num_eggs, num_floors)
    print(ans)


main()
