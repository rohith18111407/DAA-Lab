"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn\’t matter. For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5. 
"""
# Dynamic Programming Python implementation of Coin
# Change problem
"""
In Dynamic programming problems, Time Complexity is the number of unique states/subproblems * time taken per state. In this problem, for a given n, there are n unique states/subproblems. For convenience, each state is said to be solved in a constant time. Hence the time complexity is O(n * 1).
Time Complexity: O(mn),  where ‘m’ is the number of coins and ‘n’ is the target sum.
"""

def count(S, m, n):

	# table[i] will be storing the number of solutions for
	# value i. We need n+1 rows as the table is constructed
	# in bottom up manner using the base case (n = 0)
	# Initialize all table values as 0
	table = [0 for k in range(n+1)]

	# Base case (If given value is 0)
	table[0] = 1

	# Pick all coins one by one and update the table[] values
	# after the index greater than or equal to the value of the
	# picked coin
	for i in range(0,m):
		for j in range(S[i],n+1):
			table[j] += table[j-S[i]]

	return table[n]

# Driver program to test above function
arr = [1, 2, 3] #set S={S1,S2,...,Sm} of valued coins
m = len(arr)
n = 4		#Given value N
x = count(arr, m, n)
print (x)

# This code is contributed by Afzal Ansari
#Time Complexity: O(mn),  where ‘m’ is the number of coins and ‘n’ is the target sum.

"""
from typing import List
import sys
MAXINT = sys.maxsize

def coinChange(coins: List[int], amount: int) -> int:
    dp = [MAXINT]*(amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                # adding a coin of value c our bag hence adding coins req to 
                # get value a - c
                dp[a] = min( dp[a], 1 + dp[a-c])
    
    return dp[amount] if dp[amount] != MAXINT else -1


# example 2
coins = [1,3,4,5]
amount = 7
print(coinChange(coins, amount))
"""






