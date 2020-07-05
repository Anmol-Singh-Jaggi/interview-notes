'''
You are given N rectangular 3-D boxes, where the ith box has height h, width w and length l.
Your task is to create a stack of boxes which is as tall as possible, but you can only stack a box on top of
another box if the dimensions of the 2-D base of the lower box are each **strictly** larger than those of the
2-D base of the higher box.
You can rotate a box so that any side functions as its base.
It is also allowable to use multiple instances of a box; there is infinite supply of every box.

Example:
Input:
2
4
4 6 7
1 2 3
4 5 6
10 12 32
3
1 2 3
4 5 6
3 4 1

Output
60
15

SOLUTION:

Since we can rotate a box, and can use multiple instances, each rotation can be considered a
different box.
Note that since 'strictly greater' is mentioned, we cannot just literally use infinite instances.
So, generate a new array of boxes of length 3x with all the 3 base possibilities.
Then sort them according to the base area in decreasing order.
Then apply DP similar to Longest Increasing Subsequence:

dp[i] = max(dp[i], height[i] + dp[j]) for all j < i and length[j] > length[i] && width[j] > width[i]

Note that while generating box rotations, make sure to always choose length as either bigger/smaller
of length and width. It is necessary so as that we dont miss a box stacking scenario like this:

(50, 5, 10, 6)
(32, 8, 4, 10)
'''


def largest_height_subsequence(arr):
    dp = [arr[i][3] for i in range(len(arr))]
    ans = dp[0]
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j][1] > arr[i][1] and arr[j][2] > arr[i][2]:
                dp[i] = max(dp[i], dp[j] + arr[i][3])
        ans = max(ans, dp[i])
    return ans


def get_new_box(box, i, j, k):
    area = box[i] * box[j]
    height = box[k]
    # CAREFUL: max() and min() are compulsory.
    # Will get wrong answer without it.
    length = max(box[i], box[j])
    width = min(box[i], box[j])
    return (area, length, width, height)


def box_stacking_max_height(boxes):
    boxes_generated = []
    for box in boxes:
        boxes_generated.append(get_new_box(box, 0, 1, 2))
        boxes_generated.append(get_new_box(box, 0, 2, 1))
        boxes_generated.append(get_new_box(box, 1, 2, 0))
    boxes_generated.sort(reverse=True)
    return largest_height_subsequence(boxes_generated)


def main():
    boxes = []
    boxes.append((1, 2, 3))
    boxes.append((4, 6, 7))
    boxes.append((4, 5, 6))
    boxes.append((10, 12, 32))
    ans = box_stacking_max_height(boxes)
    print(ans)


main()
