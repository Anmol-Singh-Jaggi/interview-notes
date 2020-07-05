from functools import lru_cache


def maximize_screen_recursive(n, buffer_count, screen_count):
    if n < 0:
        return 0
    if n == 0:
        return screen_count
    # Just press A
    ans1 = maximize_screen_recursive(n - 1, buffer_count, screen_count + 1)
    # Press Ctrl+A, Ctrl+C, Ctrl+V
    ans2 = maximize_screen_recursive(n - 3, screen_count, screen_count * 2)
    # Press Ctrl+V
    ans3 = maximize_screen_recursive(n - 1, buffer_count, screen_count + buffer_count)
    return max(ans1, ans2, ans3)


@lru_cache(maxsize=None)
def maximize_screen_dp(n):
    # CAREFUL: Will give wrong answer if we put base case less than 4 here.
    if n <= 4:
        return n
    ans = 0
    for i in range(1, n - 2):
        possible_ans = (n - i - 1) * maximize_screen_dp(i)
        ans = max(ans, possible_ans)
    return ans


"""
Explanation for DP:

The optimal solution will have a certain 'i' keystrokes followed by
Ctrl+A, Ctrl+C and Ctrl+V, Ctrl+V, Ctrl+V, Ctrl+V.
We can just find the breakpoint 'i' at which this happens for i = 1 -> N-3.

Example: N = 10:

Lets say the answer for N=5 is ans(5).
Which means we have ans(5) characters right now on screen.
If this is the breakpoint, we'll press select and copy which will further take 2 more operations.
So total operations done are 5 + 1 + 1 = 5+2 = 7
Operations remaining = 10 - 7 = 3 which will be just used for pasting.
So we will be able to get ans(5) * 3 characters more on the screen.
But remember we had ans(5) characters on the screen already.
So total characters = ans(5) + ans(5)*3 = ans(5)[1+3] = ans(5)*4

In general, ans_at_breakpoint(i) = ans(i) + ans(i)* (n-i-2) = ans(i) * (n-i-1).
"""
