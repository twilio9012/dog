class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def kruskal_mst(self):
        mst = []
        total_cost = 0

        self.graph.sort(key=lambda x: x[2])

        ds = DisjointSet(range(1, self.V + 1))  # Handle 1-indexed vertices

        for edge in self.graph:
            u, v, w = edge
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                mst.append((u, v, w))
                total_cost += w

        return mst, total_cost

# User input for the graph
V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))
g = Graph(V)

print("Enter the details of each edge (source, destination, weight):")
for _ in range(E):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

# Calculate Minimum Spanning Tree
mst, total_cost = g.kruskal_mst()

# Output Minimum Spanning Tree and total cost
print("\nMinimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total cost:", total_cost)
