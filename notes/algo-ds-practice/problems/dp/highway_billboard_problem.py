'''
Consider a highway of M miles.
The task is to place billboards on the highway such that revenue is maximized.
The possible sites for billboards are given by number x1 < x2 < ….. < xn-1 < xn, specifying positions in miles measured from one end of the road.
If we place a billboard at position xi, we receive a revenue of ri > 0.
There is a restriction that no two billboards can be placed within t miles or less than it.

Note : All possible sites from x1 to xn are in range from 0 to M as need to place billboards on a highway of M miles.

Examples:

Input : M = 20
        x[]       = {6, 7, 12, 13, 14}
        revenue[] = {5, 6, 5,  3,  1}
        t = 5
Output: 10
By placing two billboards at 6 miles and 12 miles will produce the maximum revenue of 10.

Input : M = 15
        x[] = {6, 9, 12, 14}
        revenue[] = {5, 6, 3, 7}
        t = 2
Output : 18

SOLUTION 1:
Use DP, similar to knapsack.
For every billboard index i, we can either choose that billboard, or we can ignore it.
ans(i) = ans(j) + revenue[i], where j is the index of the closest previous billboard at a distance > t.
or ans(i) = ans(i-1).
Complexity -> O(nlogn)

Solution 2:
DP again, but this time O(M), where M is the size of the highway.
Create an array profit[] of size M such that profit[ x[i] ] = revenue[i] for all i.
Then just apply the dp:

for(int i=1;i<=x[n-1];i++)
{
    int temp = cost[i];
    if(i-t-1>=0)
        temp+=bill[i-t-1];
    bill[i]=max(bill[i-1],temp);
}
'''
