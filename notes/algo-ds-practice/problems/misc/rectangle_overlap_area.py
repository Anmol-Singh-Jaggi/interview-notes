"""
Given two rectangles, find the area of the intersection.

Note that a rectangle can be represented by two coordinates, top left and bottom right.
So mainly we are given following four coordinates.
l1: Top Left coordinate of first rectangle.
r1: Bottom Right coordinate of first rectangle.
l2: Top Left coordinate of second rectangle.
r2: Bottom Right coordinate of second rectangle.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def intersection_area(l1, r1, l2, r2):
    length = min(r1.x, r2.x) - max(l1.x, l2.x)
    breadth = min(l1.y, l2.y) - max(r1.y, r2.y)
    return length * breadth


def main():
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(5, 5)
    r2 = Point(15, 0)
    area = intersection_area(l1, r1, l2, r2)
    print(area)


main()
