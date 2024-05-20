def lcs_length(X, Y):
    if len(X) == 0 or len(Y) == 0:
        return 0
    elif X[-1] == Y[-1]:
        return lcs_length(X[:-1], Y[:-1]) + 1
    else:
        return max(lcs_length(X[:-1], Y), lcs_length(X, Y[:-1]))

X=['A','B','A','A','B','A']
Y=['B','A','B','B','A','B']
print("The longest common sub-sequence in",X,"and",Y,"is ",lcs_length(X,Y))
