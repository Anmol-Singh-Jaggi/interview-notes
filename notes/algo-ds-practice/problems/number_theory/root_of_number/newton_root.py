from algo.number_theory.newton_raphson.newton_raphson import newton_raphson


def nth_root_newton(num, n, acc=0.0000001, max_iter=10000000):
    def func(x):
        return x ** n - num

    def funcd(x):
        return n * (x ** n - 1)

    return newton_raphson(func, funcd, num / 2, acc, max_iter)


def main():
    n = 4
    root = nth_root_newton(100, n)
    print(root ** n)


if __name__ == "__main__":
    main()
