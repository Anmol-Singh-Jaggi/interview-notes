def lower_bound(items, item_to_search):
    '''
    Returns the lowest index such that items[index] >= item_to_search.
    Similar to C++ `lower_bound()` or Python `bisect_left()`.
    '''
    start_index = 0
    end_index = len(items) - 1
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        current_item = items[mid_index]
        if current_item < item_to_search:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
    return start_index


def upper_bound(items, item_to_search):
    '''
    Returns the lowest index such that items[index] > item_to_search.
    Similar to C++ `upper_bound()` or Python `bisect_right()`.
    '''
    start_index = 0
    end_index = len(items) - 1
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        current_item = items[mid_index]
        if current_item <= item_to_search:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
    return start_index


def binary_search_count(items, item_to_search):
    return upper_bound(items, item_to_search) - lower_bound(
        items, item_to_search)


def main():
    items = [1, 3, 3, 3, 5, 6]
    item = 3
    res = binary_search_count(items, item)
    print(res)


def main_file():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        items = list(map(lambda item: int(item), input().strip().split(' ')))
        item_to_search = int(input())
        res = binary_search_count(items, item_to_search)
        print(res)


if __name__ == "__main__":
    main_file()
