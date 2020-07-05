'''
Given an expression exp of length n consisting of some brackets.
The task is to print the bracket numbers when the expression is being parsed.

Example:
Input:
3​
(a+(b*c))+(d/e)​
((())(()))
((((()
Output:
1 2 2 1 3 3
1 2 3 3 2 4 5 5 4 1
1 2 3 4 5 5

Explanation:
Test case 1:The highlighted brackets in the given expression (a+(b*c))+(d/e) has been assigned the numbers as: 1 2 2 1 3 3.

SOLUTION:

Define a variable left_bnum = 1.
Create a stack right_bnum.
Now, for i = 0 to n-1.
    If exp[i] == ‘(‘, then print left_bnum, push left_bnum on to the stack right_bnum and finally increment left_bnum by 1.
    Else if exp[i] == ‘)’, then print the top element of the stack right_bnum and then pop the top element from the stack.


'''
