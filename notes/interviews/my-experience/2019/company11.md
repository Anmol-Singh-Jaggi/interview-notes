1. serialize and deserialize BST

2. https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
Solved by first inserting k pairs into a heap -> {arr1[0]*arr2[0], arr1[0]*arr2[1]... arr1[0]*arr2[k-1]}
Then pop the smallest entry {arr1[i]*arr2[j]} and insert {arr1[i]*arr2[j+1]}.
Keep doing this k times and done! 

3. https://leetcode.com/problems/find-leaves-of-binary-tree/
Just structure the code in a recursive way like most of the tree problems.
While going down the tree, return the 'level' from the children.

```python
level = max(level_left, level_right) + 1
leaves_map[level].add(root)
```

4. https://leetcode.com/problems/exclusive-time-of-functions/
Just maintain a stack and do some very simple math while iterating over the array involving current element, previous element and top of the stack.