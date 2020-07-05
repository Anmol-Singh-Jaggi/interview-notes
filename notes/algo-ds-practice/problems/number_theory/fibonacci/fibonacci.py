from functools import lru_cache


@lru_cache(maxsize=None)
def fibo(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    if n & 1:
        x = (n - 1) >> 1
        return fibo(x) ** 2 + fibo(x + 1) ** 2
    else:
        x = n >> 1
        return fibo(x) * (fibo(x + 1) + fibo(x - 1))


def main():
    for i in range(1, 10):
        print(fibo(i))


if __name__ == "__main__":
    main()
