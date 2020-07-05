"""
Given a boolean expression with the symbols 'T' and 'F', and operators '&', '|', '^' to be filled withing the operands.
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.
Let the input be in form of two arrays, one containing the symbols in order, and other contains operators.

Examples:

Input:
symbol[]    = {T, F, T}
operator[]  = {^, &}
Output: 2
The given expression is "T ^ F & T", it evaluates true in two ways "((T ^ F) & T)" and "(T ^ (F & T))"

Input:
symbol[]    = {T, F, F}
operator[]  = {^, |}
Output: 2
The given expression is "T ^ F | F", it evaluates true in two ways "( (T ^ F) | F )" and "( T ^ (F | F) )".

Input:
symbol[]    = {T, T, F, T}
operator[]  = {|, &, ^}
Output: 4
The given expression is "T | T & F ^ T", it evaluates true in 4 ways ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T)).

SOLUTION:

Let T(i,j) be the number of ways that the expression between operands i and j (inclusive) returns True.
Similarly, let F(i,j) be the number of ways for which it returns false.
Let Total(i, j) be the number of ways the expression can have any outcome.
Meaning Total(i,j) = T(i, j) + F(i, j)
Our answer will be T(0, n-1)

T(i,i) = 1 if operand is T, 0 if operand is F
F(i,i) = 0 if operand is T, 1 if operand is F

Now, we have the following recursion:
T(i,j) = Summation( T(i, j, k) ) for all k such that i < k < j
where T(i,j,k) is:
  - T(i,k) * T(k+1,j), if operator[k] == '&'
  - Total(i,k)*Total(k+1,j) - F(i,k)*F(k+1,j), if op[k] == '|'
  - T(i,k)*F(k+1,j) + F(i,k)*T(k+1,j), if op == '^'
Explanation:
expr1 & expr2 will be true when both sides are true.
expr1 | expr2 will be true in all cases except when both are false.
expr1 ^ expr2 will be true when both sides are opposite of each other.

Similarly,
F(i,j) = Summation( F(i, j, k) ) for all k such that i < k < j
where F(i,j,k) is:
  - Total(i,k)*Total(k+1,j) - T(i,k)*T(k+1,j), if operator[k] == '&'
  - F(i,k) * F(k+1,j), if op[k] == '|'
  - T(i,k)*T(k+1,j) + F(i,k)*F(k+1,j), if op == '^'
"""
from functools import lru_cache

operators = ""
operands = ""


@lru_cache(maxsize=None)
def true_ways(start, end):
    global operands, operators
    if start == end:
        return 1 if operands[start] == "T" else 0
    ans = 0
    for i in range(start, end):
        if operators[i] == "&":
            ans += true_ways(start, i) * true_ways(i + 1, end)
        elif operators[i] == "|":
            ans += total_ways(start, i) * total_ways(i + 1, end) - false_ways(
                start, i
            ) * false_ways(i + 1, end)
        else:
            ans += true_ways(start, i) * false_ways(i + 1, end) + false_ways(
                start, i
            ) * true_ways(i + 1, end)
    return ans


def total_ways(start, end):
    return true_ways(start, end) + false_ways(start, end)


@lru_cache(maxsize=None)
def false_ways(start, end):
    global operands, operators
    if start == end:
        return 1 if operands[start] == "F" else 0
    ans = 0
    for i in range(start, end):
        if operators[i] == "&":
            ans += total_ways(start, i) * total_ways(i + 1, end) - true_ways(
                start, i
            ) * true_ways(i + 1, end)
        elif operators[i] == "|":
            ans += false_ways(start, i) * false_ways(i + 1, end)
        else:
            ans += true_ways(start, i) * true_ways(i + 1, end) + false_ways(
                start, i
            ) * false_ways(i + 1, end)
    return ans


def main():
    global operands, operators
    operands = "TTFT"
    operators = "|&^"
    ans = true_ways(0, len(operands) - 1)
    print(ans)


if __name__ == "__main__":
    main()
