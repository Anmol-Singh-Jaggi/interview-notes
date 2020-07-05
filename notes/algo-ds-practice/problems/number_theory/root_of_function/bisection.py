def bisection_root(func, left, right, max_iter=100000, acc=0.0000001):
    '''
    func(left) * func(right) should be < 0 !!!
    '''
    def get_sign(num):
        return num > 0

    mid = (left + right) / 2
    value_mid = func(mid)
    while abs(value_mid) > acc and max_iter:
        if get_sign(value_mid) == get_sign(func(left)):
            left = mid
        else:
            right = mid
        mid = (left + right) / 2
        value_mid = func(mid)
        max_iter -= 1
    return mid


def func(x):
    return x ** 3 - x - 2


def main():
    ans = bisection_root(func, 1, 2)
    print(ans)
    print(func(ans))


if __name__ == "__main__":
    main()
