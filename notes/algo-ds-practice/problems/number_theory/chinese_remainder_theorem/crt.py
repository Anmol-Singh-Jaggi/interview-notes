from algo.number_theory.multiplicative_mod_inverse.multiplicative_mod_inverse import (
    mod_inverse_gcd,
)


def chinese_remainder(mods, rems):
    """
    Given 3 equations:
    x = 2 (mod 3)
    x = 3 (mod 4)
    x = 4 (mod 5)
    Solve for x.
    Easiest explanation - https://youtu.be/ru7mWZJlRQg
    Solution:
    mod_prod_total = product of all mods
    mod_prods[i] = mod_prod_total / mods[i]
    invs[i] = modinv(mod_prods[i], mods[i])
    Answer = summation(rems[i] * mod_prods[i] * invs[i]) % mod_prod_total
    NOTE: This works only if the mod values are coprime.
    Complexity -> O(nlogn)
    """
    size = len(mods)
    mod_prod_total = 1
    mod_prods = [None] * size
    invs = [None] * size
    for mod in mods:
        mod_prod_total *= mod
    for i in range(size):
        mod_prods[i] = mod_prod_total // mods[i]
    for i in range(size):
        invs[i] = mod_inverse_gcd(mod_prods[i], mods[i])
    ans = 0
    for i in range(size):
        ans += (rems[i] * mod_prods[i] * invs[i]) % mod_prod_total
    return ans % mod_prod_total


def main():
    mods = [3, 11, 13, 17]
    rems = [2, 2, 2, 2]
    crt = chinese_remainder(mods, rems)
    for i in range(len(rems)):
        print(f"{crt} % {mods[i]} = { crt % mods[i]} == {rems[i]}")


if __name__ == "__main__":
    main()
