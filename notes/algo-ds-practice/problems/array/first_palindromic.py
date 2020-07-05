from collections import Counter


def first_palindromic(str):
    '''
    There should be at most one char whose frequency is odd.
    '''
    chars_counter = Counter(str)
    odd_count = 0
    even_count = 0
    odd_char = ''
    for key, value in chars_counter.items():
        if value & 1:
            odd_char = key
            odd_count += 1
        else:
            even_count += 1
    if odd_count > 1:
        return None
    middle_element = odd_char
    chars_counter[middle_element] -= 1
    # Now all the frequencies are even.
    chars_sorted = sorted(chars_counter.keys())
    ans_list = []
    for char in chars_sorted:
        chars_counter[char] //= 2
        ans_list.extend([char] * chars_counter[char])
    ans_list.append(middle_element)
    for char in reversed(chars_sorted):
        ans_list.extend([char] * chars_counter[char])
        chars_counter[char] //= 2

    assert(not any(value > 0 for value in chars_counter.values()))
    return ''.join(ans_list)


def main():
    str = "ccbbaad"
    print(first_palindromic(str))


if __name__ == "__main__":
    main()
