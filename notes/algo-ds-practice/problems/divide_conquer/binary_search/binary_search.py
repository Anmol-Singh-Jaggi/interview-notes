def binary_search(items, item_to_search):
    start_index = 0
    end_index = len(items) - 1
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        current_item = items[mid_index]
        if current_item == item_to_search:
            return mid_index
        elif current_item < item_to_search:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
    return -1


def main():
    items = [1, 3, 5, 6]
    item = 2
    res = binary_search(items, item)
    print(res)


if __name__ == "__main__":
    main()
