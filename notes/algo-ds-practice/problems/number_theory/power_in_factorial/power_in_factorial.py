def power_in_factorial(first, second):
    denominator = second
    ans = 0
    while denominator <= first:
        ans += first // denominator
        denominator *= second
    return ans


def main():
    print(power_in_factorial(25, 5))


if __name__ == "__main__":
    main()
