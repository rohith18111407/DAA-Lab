# Depth-First Search (DFS) traversal 
# of a graph in Python using both an adjacency list and an adjacency matrix:
"""
Time Complexity of BFS = O(V+E) where V is vertices and E is edges. Time Complexity of DFS is also O(V+E) where V is vertices and E is edges
"""


import numpy as np

#---------------------------------------------------------------------------

# Using Adjacency List

# Create an adjacency list to represent the graph
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Define the DFS traversal function
def dfs_adj_list(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    
    # Base case
    if start not in visited:
        visited.add(start)
        result.append(start)
        for neighbor in graph[start]:
            dfs_adj_list(graph, neighbor, visited, result)
    
    return result

# Call the DFS traversal function and print the result
print("Using adjacency list = ",dfs_adj_list(graph, 2))

#---------------------------------------------------------------------------

# Using Adjacency Matrix

# Create an adjacency matrix to represent the graph
graph = np.array([
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
])

# Define the DFS traversal function
def dfs_adj_matrix(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    
    # Base case
    if start not in visited:
        visited.add(start)
        result.append(start)
        neighbors = np.where(graph[start] == 1)[0]
        for neighbor in neighbors:
            dfs_adj_matrix(graph, neighbor, visited, result)
    
    return result

# Call the DFS traversal function and print the result
print("Using adjacency matrix = ",dfs_adj_matrix(graph, 2))

#---------------------------------------------------------------------------

# Both implementations should produce the same result: [2, 0, 1, 3].

# Note that both implementations use recursion to traverse the graph, 
# which can be less efficient than using an iterative approach for large graphs