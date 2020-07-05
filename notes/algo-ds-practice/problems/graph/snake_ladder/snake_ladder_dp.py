from math import inf


def snake_ladder_dp(current_pos, shortcuts, cache):
    """
    All the negative shortcuts must be removed beforehand!!
    There is no point in going to a snake position.
    The minimum number of throws will never involve a snake!!
    """
    original_pos = current_pos
    while current_pos in shortcuts:
        current_pos = shortcuts[current_pos]
    if current_pos != original_pos:
        # Jump was made
        cache[original_pos] = cache[current_pos]
        return cache[original_pos]
    if current_pos == 30:
        cache[current_pos] = 0
        return 0
    ans = inf
    for dice in range(1, 7):
        next_pos = current_pos + dice
        if next_pos > 30:
            continue
        ans = min(ans, cache[next_pos] + 1)
    cache[current_pos] = ans
    return ans


def main():
    shortcuts = {}
    cache = {}
    cache[30] = 0
    for pos in range(30, 0, -1):
        snake_ladder_dp(pos, shortcuts, cache)
    print(cache[1])


main()
