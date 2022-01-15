from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.adj = defaultdict(list)
        self.num_vertices = num_vertices

    def add_edge(self, u, v, w = 0):
        self.adj[u].append((v, w))

    def print(self):
        for i in range(self.num_vertices):
            print(str(i) + ": ",end="")
            for vertex, edge_weight in self.adj[i]:
                print(f"{vertex},{edge_weight} ",end="")
            print()

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0,1,1)
    g.add_edge(0,3,2)
    g.add_edge(0,5,3)
    g.add_edge(1,2)
    g.add_edge(1,4)
    g.add_edge(2,5)
    g.add_edge(3,3)
    g.add_edge(4,1)
    g.add_edge(4,2)
    g.add_edge(4,3)
    g.add_edge(4,5)
    g.print()