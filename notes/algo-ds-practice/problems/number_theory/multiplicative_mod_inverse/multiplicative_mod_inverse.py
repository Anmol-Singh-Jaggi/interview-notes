from algo.number_theory.extended_gcd.extended_gcd import extended_gcd
from algo.number_theory.eulers_totient_function.eulers_totient import etf


def mod_inverse_gcd(a, m):
    '''
    a and m should be coprime!
    Complexity -> O(log(m)).
    '''
    return extended_gcd(a, m)[0]


def mod_inverse_eulers(a, m):
    '''
    a and m should be coprime.
    Complexity -> O(sqrt(m) + log(m)).
    '''
    etf_m = etf(m)
    return pow(a, etf_m - 1, m)


def mod_inverse_fermat(a, p):
    '''
    p must be prime and a should not be a multiple of p.
    Is a special case of Euler's Totient function actually.
    Complexity -> O(log(p)).
    '''
    return pow(a, p - 2, p)


def main():
    a = 7
    m = 5
    print(mod_inverse_gcd(7, 5))
    print(mod_inverse_fermat(7, 5))
    print(mod_inverse_eulers(7, 5))


if __name__ == "__main__":
    main()
