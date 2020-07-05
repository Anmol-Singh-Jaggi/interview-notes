'''
You are given an array A of size N. Your task is to find the length of largest dividing sub sequence.
A dividing sequence is a sequence a1, a2, …, aN where ai divides aj whenever i < j.
For example, 3, 15, 60, 720 is a dividing sequence.
input-
The first line of each test case is N, where N is the size of array.
The second line of each test case contains N space separated integers which is the input for the array.
Output-
the length of largest dividing sub sequence
examples:

    Input : arr[] = {2 11 16 12 36 60 71 17 29 144 288 129 432 993}
    Output : 5
    2 12 36 144 288 is dividing sub sequence of largest size

    Input : 1 2 4 8 16
    Output : 5
    Whole sequence is dividing

SOLUTION:

Almost similar to LIS DP.
'''
