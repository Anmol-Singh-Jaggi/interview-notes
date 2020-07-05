def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


def main():
    print(is_prime(19))


if __name__ == "__main__":
    main()
