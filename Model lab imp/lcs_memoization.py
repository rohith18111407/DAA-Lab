# Python3 program to memoize
# recursive implementation of LCS problem
maximum = 1000

# Returns length of LCS for X[0..m-1], Y[0..n-1] */
# memoization applied in recursive solution
def lcs(X, Y, m, n, dp):
	
	# base case
	if (m == 0 or n == 0):
		return 0

	# if the same state has already been
	# computed
	if (dp[m - 1][n - 1] != -1):
		return dp[m - 1][n - 1]

	# if equal, then we store the value of the
	# function call
	if (X[m - 1] == Y[n - 1]):

		# store it in arr to avoid further repetitive
		# work in future function calls
		dp[m - 1][n - 1] = 1 + lcs(X, Y, m - 1, n - 1, dp)

		return dp[m - 1][n - 1]

	else :

		# store it in arr to avoid further repetitive
		# work in future function calls
		dp[m - 1][n - 1] = max(lcs(X, Y, m, n - 1, dp),
							lcs(X, Y, m - 1, n, dp))

		return dp[m - 1][n - 1]

# Driver Code
X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)

dp = [[-1 for i in range(maximum)]
		for i in range(m)]
# print("\n",dp,"\n")

print("Length of LCS:", lcs(X, Y, m, n, dp))

# This code is contributed by Mohit Kumar
