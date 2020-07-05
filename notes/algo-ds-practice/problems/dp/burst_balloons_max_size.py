"""
Given n balloons, indexed from 0 to n-1.
Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons.
If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i.
After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1.
They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Input: [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

SOLUTION:

There are two techniques we will use to optimize our solution:

1. Divide and Conquer:
After bursting balloon i, we can divide the problem into the balloons to the left of i (nums[0:i]) and to the right of i (nums[i+1:]).
To find the optimal solution we check every optimal solution after bursting each balloon.
Since we will find the optimal solution for every range in nums, and we burst every balloon in every range to find the optimal solution, we have an O(N^2) * O(N) = O(N^3)O(N^2)∗O(N)=O(N^3) solution

However, if we try to divide our problem in the order where we burst balloons first, we run into an issue.
As balloons burst, the adjacency of other balloons changes. We are unable to keep track of what balloons the endpoints of our intervals are adjacent to.

This is where the second technique comes in.

2. Working Backwards

Above, we start with all the balloons and try to burst them.
This causes adjacency issues.
Instead, we can start with no balloons and add them in reverse order of how they were popped.
Each time we add a balloon, we can divide and conquer on its left and right sides, letting us add new balloons in between.
This gets rid of adjacency issues.
For the left interval, we know that the left boundary stays the same, and we know that our right boundary is the element we just added.
The opposite goes for the right interval.
We compute the coins added from adding balloon i with nums[left] * nums[i] * nums[right].


Approach 1: Dynamic Programming (Top-Down)

To deal with the edges of our array we can reframe the problem into only bursting the non-edge balloons and adding ones on the sides.

We define a function dp to return the maximum number of coins obtainable on the open interval (left, right).
Our base case is if there are no integers on our interval (left + 1 == right), and therefore there are no more balloons that can be added.
We add each balloon on the interval, divide and conquer the left and right sides, and find the maximum score.

The best score after adding the ith balloon is given by:

nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right)
nums[left] * nums[i] * nums[right] is the number of coins obtained from adding the ith balloon, and dp(left, i) + dp(i, right) are the maximum number of coins obtained from solving the left and right sides of that balloon respectively.

"""
from functools import lru_cache


def max_coins(nums):
    # reframe the problem
    nums = [1] + nums + [1]
    # cache this
    @lru_cache(maxsize=None)
    def dp(left, right):
        if left + 1 == right:
            return 0
        ans = 0
        for i in range(left + 1, right):
            new_ans = nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right)
            ans = max(ans, new_ans)
        return ans

    return dp(0, len(nums) - 1)


def main():
    arr = [3, 1, 5, 8]
    ans = max_coins(arr)
    print(ans)


main()
