def remove_duplicates(str, left, right):
    if right == left:
        return str[left], None
    result, last_removed = remove_duplicates(str, left + 1, right)
    if not result:
        if str[left] == last_removed:
            return '', last_removed
        else:
            return str[left], None
    if str[left] == result[0]:
        return result[1:], str[left]
    return str[left] + result, None


def main():
    str1 = "mississipie"
    # Gives wrong answer for "mississipie"
    ans = remove_duplicates(str1, 0, len(str1) - 1)
    print(ans)


main()
