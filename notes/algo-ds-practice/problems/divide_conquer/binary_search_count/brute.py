def binary_search_count_brute(items, item_to_search):
    count = 0
    for item in items:
        if item == item_to_search:
            count += 1
    return count


def main():
    items = [1, 3, 3, 3, 5, 6]
    item = 0
    res = binary_search_count_brute(items, item)
    print(res)


def main_file():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        items = map(lambda item: int(item), input().strip().split(' '))
        item_to_search = int(input())
        res = binary_search_count_brute(items, item_to_search)
        print(res)


if __name__ == "__main__":
    main_file()
