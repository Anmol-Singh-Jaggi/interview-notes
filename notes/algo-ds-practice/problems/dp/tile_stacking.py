"""
A stable tower of height n is a tower consisting of tiles of various heights stacked vertically in such a way, that no bigger tile is placed on a smaller tile.
We have infinite number of tiles of sizes 1, 2, …, m.

The task is calculate the number of different stable tower of height n that can be built from these tiles, with a restriction that you can use at most k tiles of each size in the tower.

For example:
If n = 3, m = 3 and k = 3, then ans = 3
Possible configurations:
{1, 1, 1}
{2, 1}
{3}

If n=3, m=3 and k=2, then ans = 2
{2, 1}
{3}

Note that this is different from the problem given at https://www.geeksforgeeks.org/tile-stacking-problem/
I actually read the problem incorrectly haha.

SOLUTION:
Let ans[size][top] be the number of ways to construct a tower of height 'size' with the topmost tile of height 'top'.
Then ans[size][top] = ans[size-top][top] + ans[size-top][top+1] + .... ans[size-top][m]
So we can use DP.
Final answer = ans[n][1] + ans[n][2] + ans[n][3] + .... ans[n][m]

While recursing, we can keep a 'used' hash-map maintaining the current number of tiles used of each height so far.
If at any time, the count becomes greater than k, then straightaway return 0 from there.
Complexity -> O(n*m)

Note that I haven't verified the solution anywhere, since this problem is created by me essentially!

NOTE: This is wrong solution!!
"""


def tile_stacking_ways(height, max_tile_size, max_tile_count, top, cache, used):
    if used[top] > max_tile_count:
        return 0
    if top > height:
        return 0
    if height == top:
        # We'll use a tile of size 'top' and be done with it.
        return 1
    if (height, top) in cache:
        return cache[(height, top)]
    ans = 0
    for next_top in range(top, max_tile_size + 1):
        used[next_top] = used.get(next_top, 0) + 1
        ans += tile_stacking_ways(
            height - top, max_tile_size, max_tile_count, next_top, cache, used
        )
        used[next_top] -= 1
    cache[(height, top)] = ans
    return ans


def get_ans(height, max_tile_size, max_tile_count):
    ans = 0
    cache = {}
    used = {}
    for top in range(1, max_tile_size + 1):
        used[top] = 1
        ans += tile_stacking_ways(
            height, max_tile_size, max_tile_count, top, cache, used
        )
        used[top] = 0
    print(cache)
    return ans


def main():
    height, max_tile_size, max_tile_count = 3, 3, 2
    max_tile_size = min(max_tile_size, height)
    ans = get_ans(height, max_tile_size, max_tile_count)
    print(ans)


main()
