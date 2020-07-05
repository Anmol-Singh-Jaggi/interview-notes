def binary_search(items, item_to_search, start_index, end_index):
    if start_index > end_index:
        return -1
    mid_index = (start_index + end_index) // 2
    current_item = items[mid_index]
    if current_item == item_to_search:
        return mid_index
    elif current_item < item_to_search:
        return binary_search(items, item_to_search, mid_index + 1, end_index)
    else:
        return binary_search(items, item_to_search, start_index, mid_index - 1)


def binary_search_main(items, item_to_search):
    start_index = 0
    end_index = len(items) - 1
    return binary_search(items, item_to_search, start_index, end_index)


def main():
    items = [1, 3, 5, 6]
    item = 60
    res = binary_search_main(items, item)
    print(res)


if __name__ == "__main__":
    main()
