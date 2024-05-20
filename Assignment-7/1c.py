def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    # Initialize the table to all zeros
    L = [[0] * (n+1) for i in range(m+1)]
    # Fill in the table bottom-up
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    # The length of the LCS is the value in the bottom-right corner of the table or matrix
    for i in range(m+1):
            print(L[i])
    return L[m][n]

X=['A','B','A','A','B','A']
Y=['B','A','B','B','A','B']
print("The longest common sub-sequence in",X,"and",Y,"is ",lcs_length(X,Y))
