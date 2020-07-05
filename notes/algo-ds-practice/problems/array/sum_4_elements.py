"""
Print all the quadruples in an array that sum to a given value.

"""


def sum_4_elements(arr, target):
    # Stores sum vs list of pairs for that sum.
    sums = {}
    ans = []
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            current = arr[i] + arr[j]
            rest = target - current
            lst = sums.get(rest, [])
            for idx_pair in lst:
                quadruple = (idx_pair[0], idx_pair[1], i, j)
                ans.append(quadruple)
        for k in range(0, i):
            current = arr[i] + arr[k]
            lst = sums.get(current, [])
            lst.append((k, i))
            sums[current] = lst
    return ans


def main():
    arr = [10, 2, 3, 4, 5, 9, 7, 8]
    target = 23
    ans = sum_4_elements(arr, target)
    print(ans)
    for quad in ans:
        sum = 0
        for idx in quad:
            sum += arr[idx]
        print(sum)

main()
