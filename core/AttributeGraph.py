from collections import defaultdict

# Vertex containing attributes
class Vertex:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return str(self.name) + "," + str(self.color) 

# Edge containing attributes
class Edge:
    def __init__(self, u, v, w):
        self.vertex_from = u
        self.vertex_to = v
        self.weight = w

    def __str__(self):
        return f"Edge from {self.vertex_from} to {self.vertex_to} weight {self.weight}."

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj = defaultdict(list)

    # Assuming we are given the actual Vertex objects
    def add_edge(self, u, v, w=0):
        e = Edge(u, v, w)
        self.adj[u].append(e)

    def print(self):
        for f, edge_list in self.adj.items():
            print(f"{f}: ",end="")
            for edge in edge_list:
                print(edge,end=" ")
            print()

if __name__ == "__main__":
    g = Graph(5)
    zero_vertex = Vertex("zero", "black")
    one_vertex = Vertex("one", "blue")
    two_vertex = Vertex("two", "green")
    three_vertex = Vertex("three", "gold")
    four_vertex = Vertex("four", "red")

    g.add_edge(zero_vertex,one_vertex,1)
    g.add_edge(zero_vertex,three_vertex,2)
    g.add_edge(zero_vertex,four_vertex,3)
    g.add_edge(one_vertex,two_vertex)
    g.add_edge(one_vertex,four_vertex)
    g.add_edge(two_vertex,four_vertex)
    g.add_edge(three_vertex,three_vertex)
    g.add_edge(four_vertex,one_vertex)
    g.add_edge(four_vertex,two_vertex)
    g.add_edge(four_vertex,three_vertex)

    g.print()
