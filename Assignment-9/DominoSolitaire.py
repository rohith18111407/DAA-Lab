def max_score(grid):
    n = len(grid[0])
    
    # Create a list to store the maximum scores for each column
    max_scores = [0] * (n + 1)
    
    # Base cases
    max_scores[0] = 0
    max_scores[1] = abs(grid[0][0] - grid[1][0])
    
    # Iterate over the columns, calculating the maximum score for each
    for i in range(2, n + 1):
        max_scores[i] = max(max_scores[i - 1], max_scores[i - 2] + abs(grid[0][i - 1] - grid[0][i - 2]), max_scores[i - 2] + abs(grid[1][i - 1] - grid[1][i - 2]))
    
    return max_scores[n]

# Test the implementation
grid = [[8, 6, 2, 3],
        [9, 7, 1, 2]]
result = max_score(grid)
print("Maximum score:", result)
