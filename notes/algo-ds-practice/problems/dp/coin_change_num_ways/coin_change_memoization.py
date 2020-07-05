cache = {}


def get_answer_from_cache(value, num_dens_included):
    global cache
    res = cache.get(value)
    if res is None:
        return None
    return cache.get(value).get(num_dens_included, None)


def add_to_cache(value, num_dens_included, answer):
    global cache
    res = cache.get(value)
    if res is None:
        cache[value] = {}
    cache[value][num_dens_included] = answer


def coin_change(denominations, target_value, num_dens_included=None):
    if target_value < 0 or num_dens_included == 0:
        return 0
    if target_value == 0:
        return 1
    if num_dens_included is None:
        num_dens_included = len(denominations)
    cache_answer = get_answer_from_cache(target_value, num_dens_included)
    if cache_answer is not None:
        return cache_answer
    ans = 0
    # Include the last denominations at least 1 time
    ans += coin_change(denominations,
                       target_value - denominations[num_dens_included - 1],
                       num_dens_included)
    # Exclude the last denomination
    ans += coin_change(denominations, target_value, num_dens_included - 1)
    add_to_cache(target_value, num_dens_included, ans)
    return ans


def main():
    dens = [2, 3, 5, 6]
    target_value = 10
    ans = coin_change(dens, target_value)
    print(ans)


if __name__ == "__main__":
    main()