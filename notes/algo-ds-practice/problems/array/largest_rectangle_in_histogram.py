"""
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars.
For simplicity, assume that all bars have same width and the width is 1 unit.

For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 2, 6}.
The largest possible rectangle possible is 12.

SOLUTION:

In this approach, we maintain a stack.
Initially, we push a -1 onto the stack to mark the end.
We start with the leftmost bar and keep pushing the current bar's index onto the stack until we get two successive numbers in descending order, i.e. until we get a[i] < a[i-1].

Now, we start popping the numbers from the stack until we hit a number stack[j] on the stack such that stack[j] <= stack[i]. Every time we pop, we find out the area of rectangle formed using the current element as the height of the rectangle and the difference between the the current element's index pointed to in the original array and the element stack[top-1] - stack[top−1] − 1 as the width i.e. if we pop an element stack[top] and i is the current index to which we are pointing in the original array, the current area of the rectangle will be considered as:

(i - stack[top-1] - 1) * a[stack[top]]

Further, if we reach the end of the array, we pop all the elements of the stack and at every pop, this time we use the following equation to find the area:
(stack[top]-stack[top-1]) * a[stack[top]], where stack[top] refers to the element just popped.
Thus, we can get the area of the of the largest rectangle by comparing the new area found everytime.

Explanation:

Idea is, we will consider every element a[i] to be a candidate for the area calculation.
That is, if a[i] is the minimum element then what is the maximum area possible for all such rectangles?
We can easily figure out that it's a[i]*(R-L+1-2) or a[i] * (R-L-1), where a[R] is first subsequent element(R>i) in the array just smaller than a[i], similarly a[L] is first previous element just smaller than a[i]. makes sense? (or take a[i] as a center and expand it to left and right and stop when first just smaller elements are found on both the sides).
But how to implement it efficiently?

We add the element a[i] directly to the stack if it's greater than the peak element (or a[i-1] ), because we are yet to find R for this. Can you tell what's L for this? Exactly, it's just the previous element in stack. (We will use this information later when we will pop it out).

What if we get an element a[i] which is smaller than the peak value, it is the R value for all the elements present in stack which are greater than a[i].
Pop out the elements greater than a[i], we have their R value and L value(point 2). and now push a[i] and repeat..
"""


def max_rectangle_area(heights):
    # CAREFUL: Hard implementation!
    # Giving WA on leetcode!
    stack = [-1, 0]
    max_area = 0
    for i in range(1, len(heights)):
        while len(stack) > 1 and heights[stack[-1]] >= heights[i]:
            idx = stack.pop()
            rect_height = heights[idx]
            rect_width = i - 1 - stack[-1]
            max_area = max(max_area, rect_height * rect_width)
        stack.append(i)
    while len(stack) > 1:
        idx = stack.pop()
        rect_height = heights[idx]
        rect_width = idx - stack[-1]
        max_area = max(max_area, rect_height * rect_width)
    return max_area


def main():
    heights = [2, 1, 5, 6, 2, 3]
    heights = [2, 2]
    ans = max_rectangle_area(heights)
    print(ans)


main()
