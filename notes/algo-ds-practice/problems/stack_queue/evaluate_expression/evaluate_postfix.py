def apply_operator(operand1, operator, operand2):
    operator = "//" if operator == "/" else operator
    return eval(f"{operand1} {operator} {operand2}")


def evaluate_postfix(postfix: list) -> int:
    # Expression stack will always contain just operands.
    expression_stack = []
    for i, current_element in enumerate(postfix):
        if current_element in ["+", "-", "*", "/"]:
            if len(expression_stack) == 0:
                raise Exception(f"Operand missing operands at position '{i}'")
            operand_second = expression_stack.pop()
            if len(expression_stack) == 0:
                raise Exception(f"Operand missing first operand at position '{i}'")
            operand_first = expression_stack.pop()
            result = apply_operator(operand_first, current_element, operand_second)
            expression_stack.append(result)
        else:
            expression_stack.append(current_element)
    return expression_stack.pop()


def main():
    postfix = [100, 50, "+"]
    ans = evaluate_postfix(postfix)
    print(ans)


if __name__ == "__main__":
    main()
