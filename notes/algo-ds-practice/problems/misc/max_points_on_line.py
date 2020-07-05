"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
There can be duplicate points in the input.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4

Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6


SOLUTION:
Basically use a hashmap to store <line> vs <set of points on that line>.
In a 2-D nested loop, just pair up points and keep populating the hashmap.
Take special care to get the line coefficients (Handle vertical lines and dont forget to take GCD!!).
Also, take care to handle duplicate points by just keeping a frequency counter.

Complexity -> O(n*n)
"""
from math import gcd


def get_line_coefficients(point1, point2):
    # General form of a line
    # Ax + By + C = 0
    # Derivation = https://www.geeksforgeeks.org/program-find-line-passing-2-points/
    x1, y1 = point1
    x2, y2 = point2
    a = y1 - y2
    b = x2 - x1
    c = x2 * y1 - x1 * y2
    # CAREFUL
    abc_gcd = gcd(gcd(a, b), c)
    if abc_gcd:
        a = a // abc_gcd
        b = b // abc_gcd
        c = c // abc_gcd
    return (a, b, c)


def max_points_on_line(points):
    # Warning: Giving WA on Leetcode!
    lines = {}
    points_freq = {}
    for i in range(0, len(points)):
        freq = points_freq.get(points[i], 0)
        points_freq[points[i]] = freq + 1
        for j in range(i + 1, len(points)):
            point1 = points[i]
            point2 = points[j]
            line_coeffs = get_line_coefficients(point1, point2)
            line_set = lines.get(line_coeffs, set())
            line_set.add(point1)
            line_set.add(point2)
            lines[line_coeffs] = line_set
    ans = 0
    for points in lines.values():
        line_size = 0
        for point in points:
            line_size += points_freq.get(point)
        ans = max(ans, line_size)
    if ans == 0 and len(points) >= 1:
        # No line exists!
        ans = 1
    return ans


def main():
    points = [(1, 1), (2, 2), (3, 3), (1, 1)]
    points = [(0, 0), (-1, -1), (2, 2)]
    ans = max_points_on_line(points)
    print(ans)


main()
