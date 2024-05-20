size = [0]*100000

parent = [0]*100000

ans = []

def make(node):
    parent[node] = node
    size[node] = 1

def getparent(node):
    if parent[node]==node:
        return node
    else:
        parent[node] = parent[parent[node]]
        return getparent(parent[node])

def union(a,b):
    par_a = getparent(a)
    par_b = getparent(b)

    if par_a != par_b:
        if size[par_a]<size[par_b]:

            parent[par_a] = par_b
            size[par_b] +=1
        else:
            parent[par_b] = par_a
            size[par_a] +=1


m = int(input("enter the no of node"))
for i in range(m):
    a = int(input("enter the node"))
    make(a)


n = int(input("enter the number of edges "))
graph=[]
for i in range(n):
    wt = int(input(" enter the weight of the edge"))
    a= int(input("enter node1 "))
    b=int(input("enter node2 "))
    graph.append((wt,(a,b)))
graph = sorted(graph)

print(graph)


mst = []

for i in graph: 
    node1 = i[1][0]
    node2 = i[1][1]
    print(node1)
    print(node2)

    if getparent(node1) == getparent(node2):
        continue
    else:
        union(node1,node2)
        ans.append((node1,node2))

print(ans)