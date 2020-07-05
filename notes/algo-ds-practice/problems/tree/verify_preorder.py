"""
One way to serialize a binary tree is to use pre-order traversal.
When we encounter a non-null node, we record the node's value.
If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#"
where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal
serialization of a binary tree. Find an algorithm without reconstructing the tree.
Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid,
for example it could never contain two consecutive commas such as "1,,3".


Example 1:
Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true

Example 2:
Input: "1,#"
Output: false

Example 3:
Input: "9,#,#,1"
Output: false


SOLUTION:

Binary tree could be considered as a number of slots to fulfill.
At the start there is just one slot available for a number or null node.
Both number and null node take one slot to be placed.
For the null node the story ends up here, whereas the number will add into the tree two slots for the child nodes.
Each child node could be, again, a number or a null.

The idea is straightforward: take the nodes one by one from preorder traversal,
and compute the number of available slots.
If at the end all available slots are used up, the preorder traversal represents the valid serialization.

In the beginning there is one available slot.
Each number or null consumes one slot.
Null node adds no slots, whereas each number adds two slots for the child nodes.
"""


def is_valid_preorder(preorder):
    preorder = preorder.split(",")
    # CAREFUL: Its 1 initially!
    slots = 1
    for i in range(len(preorder)):
        val = preorder[i]
        slots -= 1
        # CAREFUL: This is important!
        if slots < 0:
            return False
        if val != "#":
            slots += 2
    return slots == 0


def main():
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    print(is_valid_preorder(preorder))
    preorder = "1,#"
    print(is_valid_preorder(preorder))
    preorder = "9,#,#,1"
    print(is_valid_preorder(preorder))


main()
