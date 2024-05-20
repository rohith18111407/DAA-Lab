#Breadth-First Search (BFS) traversal 
# of a graph in Python using both an adjacency list and an adjacency matrix:

"""
Time Complexity of BFS = O(V+E) where V is vertices and E is edges. Time Complexity of DFS is also O(V+E) where V is vertices and E is edges
"""

from collections import deque
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

# Define the BFS traversal function
def bfs_adj_list(graph, start):
    # Initialize visited, queue and result list
    visited = set()
    queue = deque([start])
    result = []
    
    # BFS algorithm
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])
    
    return result

# Call the BFS traversal function and print the result
print("Using adjacency list = ",bfs_adj_list(graph, 2))


#--------------------------------------------------------------------------------

# Create an adjacency matrix to represent the graph
graph = np.array([
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
])

# Define the BFS traversal function
def bfs_adj_matrix(graph, start):
    # Initialize visited, queue and result list
    visited = set()
    queue = deque([start])
    result = []
    
    # BFS algorithm
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            neighbors = np.where(graph[node] == 1)[0]
            queue.extend(neighbors)
    
    return result

# Call the BFS traversal function and print the result
print("Using adjacency matrix = ",bfs_adj_matrix(graph, 2))

#-----------------------------------------------------------------------------

# Both implementations should produce the same result: [2, 0, 3, 1].