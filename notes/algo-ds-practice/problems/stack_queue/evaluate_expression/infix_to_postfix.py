import re
from problems.stack_queue.evaluate_expression.evaluate_postfix import evaluate_postfix


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


def greater_precedence(op1, op2):
    precedences = {"+": 0, "-": 0, "*": 1, "/": 1}
    return precedences[op1] > precedences[op2]


def infix_to_postfix(expression):
    tokens = re.findall("[+/*()-]|\d+", expression)
    operators = []
    output = []
    for token in tokens:
        if is_number(token):
            output.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            top = peek(operators)
            while top != "(":
                output.append(operators.pop())
                top = peek(operators)
            operators.pop()
        else:
            # Its an operator
            # CAREFUL : This is the only tricky case!
            top = peek(operators)
            while top is not None and top != "(" and greater_precedence(top, token):
                output.append(operators.pop())
                top = peek(operators)
            operators.append(token)
    while peek(operators) is not None:
        output.append(operators.pop())
    return output


def main():
    expression = "((20 - 10 ) * (30 - 20) )"
    expression = "100+50*9-2"
    postfix = infix_to_postfix(expression)
    print(postfix)
    print("Shunting Yard Algorithm: {0}".format(evaluate_postfix(postfix)))
    print("Python: {0}".format(eval(expression)))


if __name__ == "__main__":
    main()
