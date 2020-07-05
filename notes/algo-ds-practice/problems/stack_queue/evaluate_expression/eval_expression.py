from problems.stack_queue.evaluate_expression.evaluate_postfix import evaluate_postfix
from problems.stack_queue.evaluate_expression.infix_to_postfix import infix_to_postfix


def sanitize(infix_expression_string):
    return infix_expression_string.replace(' ', '')


def evaluate_expression(expression):
    expression = sanitize(expression)
    postfix = infix_to_postfix(expression)
    final_result = evaluate_postfix(postfix)
    return final_result


def main():
    expression = "1 +2 *3 - (6/3)"
    ans = evaluate_expression(expression)
    print(ans)
