from random import randint


def fisher_yates_shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        rand_idx = randint(0, i)
        arr[i], arr[rand_idx] = arr[rand_idx], arr[i]


def main():
    arr = [1, 2, 3, 4]
    fisher_yates_shuffle(arr)
    print(arr)


main()
