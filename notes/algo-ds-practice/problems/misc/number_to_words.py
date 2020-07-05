ones = [
    "",
    "one ",
    "two ",
    "three ",
    "four ",
    "five ",
    "six ",
    "seven ",
    "eight ",
    "nine ",
    "ten ",
    "eleven ",
    "twelve ",
    "thirteen ",
    "fourteen ",
    "fifteen ",
    "sixteen ",
    "seventeen ",
    "eighteen ",
    "nineteen ",
]

tens = [
    "",
    "",
    "twenty ",
    "thirty ",
    "forty ",
    "fifty ",
    "sixty ",
    "seventy ",
    "eighty ",
    "ninety ",
]


def two_digit_to_words(num, word):
    if num == 0:
        return ""
    str = ""
    if num > 19:
        str += tens[num // 10] + ones[num % 10]
    else:
        str += ones[num]
    if num:
        str += word
    return str


def convert_number_to_words(n):
    if n == 0:
        return "zero"
    out = ""
    out += two_digit_to_words((n // 10000000), "crore ")
    out += two_digit_to_words(((n // 100000) % 100), "lakh ")
    out += two_digit_to_words(((n // 1000) % 100), "thousand ")
    out += two_digit_to_words(((n // 100) % 10), "hundred ")
    if n > 100 and n % 100:
        out += "and "
    out += two_digit_to_words((n % 100), "")
    return out


def main():
    num = 653536
    print(convert_number_to_words(num))


main()
