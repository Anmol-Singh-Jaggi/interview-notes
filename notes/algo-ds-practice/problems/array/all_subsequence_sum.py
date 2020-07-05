'''
Solution 1:
Let sum[i] = Sum of all subsequences containing element n[i] with any of the previous elements.
Let num[i] = Number of subsequences from 0 till i inclusive = 2^(i+1)
sum[i] = sum[i-1] + num[i-1] * n[i] (Since we can append n[i] to all the num[i-1] sequences)
sum[i] = sum[i-1] + 2^(i) * n[i]
ans[i] = ans[i-1] + sum[i] (The subsequences covered by the sum[i]'s are all unique and separate.)
Answer = sum[0] + sum[1] + ...

Solution 2:

All the elements occur exactly 2^(n-1) times in the resultant power set.
Draw a boolean truth table to prove this.
So answer = (sum of all elements) * 2^(n-1)
'''
