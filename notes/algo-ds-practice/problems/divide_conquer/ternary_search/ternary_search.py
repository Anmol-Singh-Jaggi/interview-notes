from functools import partial


def ternary_search(func, low, high, precision, max_iterations):
    """
    Returns tha maxima of the function `func` given the range
    `low` - `high` within the specified `precision` stopping
    after `max_iterations`.
    Returns -1 if the precision could not be achieved withing `max_iterations`
    """
    maxima = -1
    while max_iterations > 0:
        point1 = low + (high - low) / 3
        point2 = high - (high - low) / 3
        # CAREFUL: The precision is between the x values not y!
        if abs(point1 - point2) <= precision:
            maxima = (point1 + point2) / 2
            break
        f_point2 = func(point2)
        f_point1 = func(point1)
        if f_point2 > f_point1:
            low = point1
        else:
            high = point2
        max_iterations -= 1
    return maxima


def function_to_maximize(x):
    return -x * x + 5 * x + 10


def expo_search(ternary_search_function):
    """
    Find how much iterations does it take for `ternary_search`
    to find the answer.
    Iteratively increase the `max_iterations` parameter by a factor of 2
    until we find the ternary search starts to give a valid answer.
    After that, just binary search within that range.
    """
    num_iterations_lower_bound = 1
    num_iterations_upper_bound = num_iterations_lower_bound
    while True:
        search_result = ternary_search_function(
            max_iterations=num_iterations_upper_bound
        )
        if search_result != -1:
            break
        num_iterations_upper_bound *= 2
    # We can increment the lower bound here as well!
    num_iterations_lower_bound = num_iterations_upper_bound // 2
    # Now just do binary search
    while num_iterations_upper_bound >= num_iterations_lower_bound:
        mid = (num_iterations_lower_bound + num_iterations_upper_bound) // 2
        evalu = ternary_search_function(max_iterations=mid)
        if evalu == -1:
            num_iterations_lower_bound = mid + 1
        else:
            num_iterations_upper_bound = mid - 1
    return num_iterations_lower_bound


def main():
    # We can apply exponential search here to get the
    # number of iterations required to get an answer
    ternary_search_partial = partial(
        ternary_search,
        func=function_to_maximize,
        low=-5000,
        high=5000,
        precision=0.00000001,
    )
    num_iter = expo_search(ternary_search_partial)
    print(num_iter)
    maxima = ternary_search_partial(max_iterations=num_iter - 1)
    print(maxima)
    maxima = ternary_search_partial(max_iterations=num_iter)
    print(maxima)


if __name__ == "__main__":
    main()
