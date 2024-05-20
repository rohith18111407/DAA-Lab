"""
O(E logE) or O(V logV) is the time complexity of the Kruskal algorithm.
T(n)=2T(n/2)+n
"""

# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph


class Graph():  
    def __init__(self, vertices):  
        self.vertices = vertices  
        self.edges = []  
        self.adjacency_list = {v: [] for v in vertices}  
  
    def addEdge(self, u, v, weight):  
        self.edges.append((u, v, weight))  
        self.adjacency_list[u].append((v, weight))  
        self.adjacency_list[v].append((u, weight))  
  
    def find_parent(self, parent, i):  
        if parent[i] == i:  
            return i  
        return self.find_parent(parent, parent[i])  
  
    def union(self, parent, rank, x, y):  
        root_x = self.find_parent(parent, x)  
        root_y = self.find_parent(parent, y)  
        if rank[root_x] < rank[root_y]:  
            parent[root_x] = root_y  
        elif rank[root_x] > rank[root_y]:  
            parent[root_y] = root_x  
        else:  
            parent[root_y] = root_x  
            rank[root_x] += 1  
  
    def kruskal(self):  
        minimum_spanning_tree = set()  
        parent = {}  
        rank = {}  
        for v in self.vertices:  
            parent[v] = v  
            rank[v] = 0  
        sorted_edges = sorted(self.edges, key=lambda x: x[2])  
        for edge in sorted_edges:  
            u, v, weight = edge  
            root_u = self.find_parent(parent, u)  
            root_v = self.find_parent(parent, v)  
            if root_u != root_v:  
                minimum_spanning_tree.add(edge)  
                self.union(parent, rank, root_u, root_v)  
        return minimum_spanning_tree  
vertices = [0, 1, 2, 3]  
g = Graph(vertices)  
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
minimum_spanning_tree = g.kruskal()  
print(minimum_spanning_tree)  


"""
# Class to represent a graph
class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = []

	# Function to add an edge to graph
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	# A utility function to find set of an element i
	# (truly uses path compression technique)
	def find(self, parent, i):
		if parent[i] != i:

			# Reassignment of node's parent
			# to root node as
			# path compression requires
			parent[i] = self.find(parent, parent[i])
		return parent[i]

	# A function that does union of two sets of x and y
	# (uses union by rank)
	def union(self, parent, rank, x, y):

		# Attach smaller rank tree under root of
		# high rank tree (Union by Rank)
		if rank[x] < rank[y]:
			parent[x] = y
		elif rank[x] > rank[y]:
			parent[y] = x

		# If ranks are same, then make one as root
		# and increment its rank by one
		else:
			parent[y] = x
			rank[x] += 1

	# The main function to construct MST
	# using Kruskal's algorithm
	def KruskalMST(self):

		# This will store the resultant MST
		result = []

		# An index variable, used for sorted edges
		i = 0

		# An index variable, used for result[]
		e = 0

		# Sort all the edges in
		# non-decreasing order of their
		# weight
		self.graph = sorted(self.graph,
							key=lambda item: item[2])

		parent = []
		rank = []

		# Create V subsets with single elements
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# Number of edges to be taken is less than to V-1
		while e < self.V - 1:

			# Pick the smallest edge and increment
			# the index for next iteration
			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			# If including this edge doesn't
			# cause cycle, then include it in result
			# and increment the index of result
			# for next edge
			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)
			# Else discard the edge

		minimumCost = 0
		print("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Minimum Spanning Tree", minimumCost)


# Driver code
if __name__ == '__main__':
	g = Graph(4)
	g.addEdge(0, 1, 10)
	g.addEdge(0, 2, 6)
	g.addEdge(0, 3, 5)
	g.addEdge(1, 3, 15)
	g.addEdge(2, 3, 4)

	# Function call
	g.KruskalMST()


g = Graph(6)

g.addEdge(6, 1, 60)
g.addEdge(1, 2, 10)
g.addEdge(2, 3, 20)
g.addEdge(3, 4, 30)
g.addEdge(4, 5, 40)
g.addEdge(5,6,50)
g.addEdge(3,6,15)
g.addEdge(2,5,25)

# Function call
g.KruskalMST()
"""


