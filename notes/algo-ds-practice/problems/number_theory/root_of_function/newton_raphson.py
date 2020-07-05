def newton_raphson(func, funcd, initial_guess=1, acc=0.000001, max_iter=100000):
    """
    func -> Function to find root of
    funcd -> Derivative of function
    It does not work all the time!!
    """
    guess = initial_guess
    # CAREFUL: Dont forget abs()!!
    while abs(func(guess)) > acc and max_iter >= 0:
        guess -= func(guess) / funcd(guess)
        max_iter += 1
    return guess


def func(x):
    return x ** 3 + 56 * x - 100


def funcd(x):
    return 3 * (x ** 2) + 56


def main():
    ans = newton_raphson(func, funcd, 100)
    print(ans)
    print(func(ans))


if __name__ == "__main__":
    main()
