import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

graph = np.array([
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
])

# Create a directed graph from the adjacency matrix
G = nx.from_numpy_matrix(graph, create_using=nx.DiGraph)

# Draw the graph
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, arrowsize=20, font_size=12)

# Display the graph
plt.show()
