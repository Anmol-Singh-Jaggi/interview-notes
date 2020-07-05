def generate_subseq_with_sum(arr, sum):
    if not arr and sum == 0:
        return [[]]
    if not arr:
        return None
    # Include the last element
    result = []
    if sum >= arr[-1]:
        including_last = generate_subseq_with_sum(arr[: len(arr) - 1], sum - arr[-1])
        if including_last is not None:
            for seq in including_last:
                seq.append(arr[-1])
            result += including_last
    # Exclude the last element
    excluding_last = generate_subseq_with_sum(arr[: len(arr) - 1], sum)
    if excluding_last is not None:
        result += excluding_last
    return result


def generate_subseq_with_sum_iterator(arr, sum):
    if not arr and sum == 0:
        yield []
        return
    if not arr:
        yield None
        return
    # Include the last element
    if sum >= arr[-1]:
        including_last = generate_subseq_with_sum_iterator(
            arr[: len(arr) - 1], sum - arr[-1]
        )
        if including_last is not None:
            for seq in including_last:
                if seq is not None:
                    yield seq + [arr[-1]]
    # Exclude the last element
    excluding_last = generate_subseq_with_sum_iterator(arr[: len(arr) - 1], sum)
    if excluding_last is not None:
        for seq in excluding_last:
            if seq is not None:
                yield seq


def main():
    arr = [int(x) for x in "10 1 2 7 6 1 5".split()]
    sum = 8
    ans = generate_subseq_with_sum(arr, sum)
    ans = [tuple(sorted(x)) for x in ans]
    ans = list(set(ans))
    ans.sort()
    print(ans)

    ans = generate_subseq_with_sum_iterator(arr, sum)
    ans = list(ans)
    ans = [tuple(sorted(x)) for x in ans]
    ans = list(set(ans))
    ans.sort()
    print(ans)


main()
