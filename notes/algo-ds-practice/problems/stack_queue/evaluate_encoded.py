"""
Decode the encoded string.
For example:

Input = 3[b2[ca]]
output = bcacabcacabcaca

Input = 2[asa]
Output = asaasa
"""


def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def peek(stack):
    return stack[-1] if stack else None


def decode(expression):
    numbers = []
    alphas = []
    for token in expression:
        if is_number(token):
            numbers.append(int(token))
        elif token == "[":
            alphas.append(token)
        elif token == "]":
            top = peek(alphas)
            last_string = ""
            while top is not None and top != "[":
                alphas.pop()
                last_string += top
                top = peek(alphas)
            alphas.pop()  # Discard the '['
            last_multiplier = int(numbers.pop())
            last_string = last_string[::-1]
            for i in range(last_multiplier):
                for ch in last_string:
                    alphas.append(ch)
        else:
            alphas.append(token)
    output = []
    while peek(alphas) is not None:
        output.append(alphas.pop())
    output = output[::-1]
    return "".join(output)


def main():
    expression = "3[b2[ca]]"
    # expression = "2[asa]"
    decoded = decode(expression)
    print(decoded)


if __name__ == "__main__":
    main()
