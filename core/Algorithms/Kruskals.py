import heapq
from collections import deque

class UnionFind:
    # Constructor O(N)
    def __init__(self, universe: list):
        self._parent = {} # Parent Links
        self._rank = {}   # Number of nodes in tree rooted by parent
        self._num_components = len(universe)

        # Initialize the disjoint forest such that each node
        # in the universe is its own parent with a rank of 1
        for value in universe:
            self._parent[value] = value
            self._rank[value] = 1

    def count(self) -> int:
        return self._num_components

    def connected(self, p, q) -> bool:
        return self._find(p) == self._find(q)

    # Recursive path compression
    # inverse Ackermann so nearly constant time
    def _find(self, p):
        if p != self._parent[p]:
            self._parent[p] = self._find(self._parent[p])
        return self._parent[p]

    # inverse Ackermann so nearly constant time
    def union(self, p, q):
        if self.connected(p, q):
            return

        # Make smaller root point to larger one
        if self._rank[p] < self._rank[q]:
            self._parent[p] = q
            self._rank[q] += self._rank[p]
        else:
            self._parent[q] = p
            self._rank[p] += self._rank[q]
        
        self._num_components -= 1

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def other(self, v):
        if v == self.v: return self.w
        elif v == self.w: return self.v
        else: raise RuntimeError("Inconsistent edge")

# MSP algorithms only work on undirected graphs
class Graph:
    def __init__(self, vertices: list):
        self.adj = {}
        self.num_edges = 0
        self.num_vertices = len(vertices)
        for vertex in vertices:
            self.adj[vertex] = list()

    def addEdge(self, edge: Edge):
        self.adj[edge.v].append(edge)
        self.adj[edge.w].append(edge)
        self.num_edges += 1

    def adjacentEdges(self, vertex):
        return self.adj[vertex]

    def edges(self):
        e = []
        for vertex, adj_list in self.adj.items():
            for edge in adj_list:
                if edge.other(vertex) > vertex:
                    e.append(edge)

        return e

class KruskalMST:
    def __init__(self, graph):
        # Represents our queue of selected edges
        self.mst = deque() 
        self.weight = 0

        # Create our pq of edges to choose from
        min_pq = []
        all_edges = graph.edges()
        for edge in all_edges:
            heapq.heappush(min_pq, (edge.weight, edge))

        # Create our UnionFind datastructure for cycle detection
        uf = UnionFind(graph.adj.keys())

        while len(min_pq) > 0 and len(self.mst) < graph.num_vertices - 1:
            # Pull of the min edge and get the two associated vertices
            edge = heapq.heappop(min_pq)[1]
            v = edge.v
            w = edge.w

            # Ignore edges that would create a cycle (both exist in the same connected component)
            if uf.connected(v, w):
                continue

            # Choose this edge and add it to our mst and the connected component
            uf.union(v, w)
            self.mst.append(edge)
            self.weight += edge.weight

    def edges(self):
        return list(self.mst)

if __name__ == "__main__":
    universe = [0,1,2,3,4,5,6,7]
    graph = Graph(universe)
    graph.addEdge(Edge(0, 7, 0.16))
    graph.addEdge(Edge(2, 3, 0.17))
    graph.addEdge(Edge(1, 7, 0.19))
    graph.addEdge(Edge(0, 2, 0.26))
    graph.addEdge(Edge(5, 7, 0.28))
    graph.addEdge(Edge(4, 5, 0.35))
    graph.addEdge(Edge(6, 2, 0.40))

    mst = KruskalMST(graph)
    print(mst.weight)
    for node in mst.edges():
        print(str(node.v) + "-" + str(node.w))