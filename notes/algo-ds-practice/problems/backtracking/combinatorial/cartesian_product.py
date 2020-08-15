def cartesian_product(sizes, start=0):
    if not sizes:
        return []
    if start == len(sizes) - 1:
        return [[i] for i in range(sizes[-1])]
    sub_answer_lists = cartesian_product(sizes, start+1)
    ans = []
    for sub_ans_list in sub_answer_lists:
        for j in range(sizes[start]):
            list_copy = [j]
            list_copy.extend(sub_ans_list)
            ans.append(list_copy)
    return ans


def cartesian_product_generator(sizes, start=0):
    if not sizes:
        yield []
        return
    if start == len(sizes) - 1:
        for i in range(sizes[-1]):
            yield [i]
        return
    for sub_ans_list in cartesian_product_generator(sizes, start+1):
        for j in range(sizes[start]):
            list_copy = [j]
            list_copy.extend(sub_ans_list)
            yield list_copy


def main():
    # Useful in taking cartesian product of 2 lists of sizes 2 and 6.
    for elem in cartesian_product_generator([2, 6]):
        print(elem)


if __name__ == "__main__":
    main()
