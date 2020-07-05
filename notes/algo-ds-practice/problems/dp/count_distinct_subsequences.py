'''
Given a string, find the number of distinct subsequences of that string.

SOLUTION:

If the characters in the string are all distinct, then the answer will be simple:
nC0  + nC1 + nC2 + .... nCn  = 2n where n is the length of the string.

let us try to analyze what happens when we add a new character that already exists.
we take an example string "xabcb"
step 1) we have x, this accounts for 2 subsequences which are  {x,Ø}.
step 2) we have xa, this accounts for 4 = 2*2 subsequences which are {x,a,xa,Ø}.
step 3) we have xab, this accounts for 8 = 2*4 subsequences which are {x,a,b,xa,ab,xb,xab,Ø}.
step 4) we have xabc, this accounts for 16 = 2*8 subsequences which are {x,a,b,xa,ab,xb,xab,Ø,xc,ac,bc,xac,abc,xbc,xabc,c}.
up to step 4, we can see that the answer gets doubled when we add characters that haven't already appeared.
step 5) we have xabcb, first we double the last answer to get 32. But in this way, we are overcounting. For example xab is counted twice (once with the first occurence of b and then once with the second occurence of b).

We always keep track of the last occurence of each character.
What are the cases which we have overcounted?
Well they come from the part  of the string just before our last occurence of b : "xa". for xa, the answer was 4. so we have counted each of these 4 subsequences twice: {xb, ab, b, xab}.
We subtract this from our present answer to get 32 - 4 = 28 which is the answer.

Let:
dp[i] = number of distinct subsequences ending with a[i]
sum[i] = dp[1] + dp[2] + ... + dp[i]. So sum[n] will be your answer.
last[i] = last position of character i in the given string.
A null string has one subsequence, so dp[0] = 1.

for i = 1 to n
  dp[i] = sum[i - 1] - sum[last[a[i]] - 1]
  sum[i] = sum[i - 1] + dp[i]
  last[a[i]] = i

return sum[n]
'''
