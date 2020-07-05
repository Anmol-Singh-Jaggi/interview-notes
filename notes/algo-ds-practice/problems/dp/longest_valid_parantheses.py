'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

SOLUTION:
Maintain a stack which has the indices of all unmatched '('.
Also maintain a dp array such that dp[i] = longest valid parentheses ending at i.
dp[i] will always be 0 if str[i] == '('.
Now, dp[i] = i - stack.top() + 1 + ans[stack.top()-1].
ans[stack.top()-1] signifies the answer for the string just before the last matching '(' character.
Final answer is max(dp).
'''


def longest_valid_parantheses(str):
    if not str:
        return 0
    ans = [0] * len(str)
    stack = []
    for i in range(len(str)):
        ch = str[i]
        if ch == '(':
            stack.append(i)
        else:
            if not stack:
                pass
            else:
                top = stack.pop()
                ans[i] = i - top + 1
                if top > 0:
                    ans[i] += ans[top-1]
    return max(ans)


def main():
    str = ')()())'
    str = '((()'
    str = '(()))'
    str = ''
    ans = longest_valid(str)
    print(ans)

main()
