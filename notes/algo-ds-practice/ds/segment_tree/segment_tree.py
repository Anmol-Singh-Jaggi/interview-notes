import sys
from math import inf
sys.setrecursionlimit(1000000)


class SegmentTree:
    def __init__(self, arr):
        self.arr = list(arr)
        self.tree = [None] * len(arr) * 2
        self.build_tree(1, 0, len(arr) - 1)
        self.qleft = None
        self.qright = None
        self.val = None

    def _left_child(self, node):
        return node * 2

    def _right_child(self, node):
        return self._left_child(node) + 1

    def build_tree(self, node, left, right):
        if left == right:
            self.tree[node] = self.arr[left]
            return
        mid = (left + right) // 2
        left_child = self._left_child(node)
        right_child = self._right_child(node)
        self.build_tree(left_child, left, mid)
        self.build_tree(right_child, mid + 1, right)
        self.tree[node] = max(self.tree[left_child], self.tree[right_child])

    def _update(self, node, left, right):
        if self.qright < left or self.qleft > right:
            return
        if left == right:
            self.tree[node] += self.val
            return
        mid = (left + right) // 2
        left_child = self._left_child(node)
        right_child = self._right_child(node)
        self._update(left_child, left, mid)
        self._update(right_child, mid + 1, right)
        self.tree[node] = max(self.tree[left_child], self.tree[right_child])

    def _query(self, node, left, right):
        if self.qright < left or self.qleft > right:
            return -inf
        if left >= self.qleft and right <= self.qright:
            return self.tree[node]
        mid = (left + right) // 2
        ans_left = self._query(self._left_child(node), left, mid)
        ans_right = self._query(self._right_child(node), mid + 1, right)
        return max(ans_left, ans_right)

    def query(self, qleft, qright):
        self.qleft = qleft
        self.qright = qright
        return self._query(1, 0, len(self.arr) - 1)

    def update(self, qleft, qright, val):
        self.qleft = qleft
        self.qright = qright
        self.val = val
        self._update(1, 0, len(self.arr) - 1)


def main():
    arr = [1, 2, 3, 4, 5]
    seg_tree = SegmentTree(arr)
    seg_tree.update(0, 5, 1)
    ret = seg_tree.query(1, 3)
    print(ret)


if __name__ == "__main__":
    main()
