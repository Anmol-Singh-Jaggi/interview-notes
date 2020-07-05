import re


def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def is_name(str):
    return re.match("\w+", str)


def peek(stack):
    return stack[-1] if stack else None


def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    values.append(eval("{0}{1}{2}".format(left, operator, right)))


def greater_precedence(op1, op2):
    precedences = {"+": 0, "-": 0, "*": 1, "/": 1}
    return precedences[op1] > precedences[op2]


def evaluate(expression):
    """
    Exactly same as shunting yard.
    Just replace `output.append(operators.pop())` with
    `apply_operator(operators, values)`
    """
    tokens = re.findall("[+/*()-]|\d+", expression)
    values = []
    operators = []
    for token in tokens:
        if is_number(token):
            values.append(int(token))
        elif token == "(":
            operators.append(token)
        elif token == ")":
            top = peek(operators)
            while top is not None and top != "(":
                apply_operator(operators, values)
                top = peek(operators)
            operators.pop()  # Discard the '('
        else:
            # Operator
            top = peek(operators)
            while top is not None and top != "(" and greater_precedence(top, token):
                apply_operator(operators, values)
                top = peek(operators)
            operators.append(token)
    while peek(operators) is not None:
        apply_operator(operators, values)

    return values[0]


def main():
    expression = "((20 - 10 ) * (30 - 20) / 10 + 10 ) * 2"
    print("Shunting Yard Algorithm: {0}".format(evaluate(expression)))
    print("Python: {0}".format(eval(expression)))


if __name__ == "__main__":
    main()
