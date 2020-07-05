"""
Let dp[i] = sum of all subarrays ending at i.
dp[i] = dp[i-1] + n[i]*(i+1)
answer = dp[0] + dp[1] + ... dp[n-1]
"""
