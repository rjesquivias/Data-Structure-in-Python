from collections import defaultdict
from collections import deque
import sys

# Adjacency List representation in Python
class VertexAttributes:
    def __init__(self, color="white", distance=sys.maxsize, parent=None):
        self.color = color
        self.distance = distance
        self.parent = parent

    def __str__(self):
        return str("color: " + str(self.color) + " | distance: " + str(self.distance) + " | parent: " + str(self.parent))

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Add edges
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Print the graph
    def print_graph(self):
        for vertex in self.graph:
            print(str(vertex) + ":", end=" ")
            for node in self.graph[vertex]:
                print("--> " + str(node), end=" ")
            print()

    # In this representation of a graph, our adjacency list uses integer values
    # to identify which nodes are connected. Since we aren't keeping track of actual
    # 'Node' objects, any auxillary data that we may want to track will need to be created
    # in a new list or data structure.
    #
    # e.g. we want to track color, distance, and parent below, so we create an auxillary list 
    #      of VertexAttributes objects that are used to hold the data.
    #
    # Note: We wouldn't need to create this auxillary data structure in the object oriented
    #       graph approach where we store the list of adjacent nodes within the Node objects
    #       themselves
    def BFS(self, source):
        # Initialize our auxillary data structures for each vertex
        vertex_attributes = defaultdict(VertexAttributes)

        for vertex in self.graph:
            # Create our VertexAttribute object
            vertex_attribute = VertexAttributes()
            vertex_attribute.color = "white"
            vertex_attribute.distance = sys.maxsize
            vertex_attribute.parent = None
            # Store the data using the vertices index value as a key
            vertex_attributes[vertex] = vertex_attribute

        # Source vertex data initialization
        vertex_attributes[source].color = "gray"
        vertex_attributes[source].distance = 0

        # Standard BFS
        q = deque()
        q.append(source)
        while len(q) != 0:
            parent = q.popleft()
            print(str(parent), end=" ")
            print(vertex_attributes[parent])
            for adjacent_vertex in self.graph[parent]:
                attributes = vertex_attributes[adjacent_vertex]
                # We are using the color attribute as a replacement for a 'seen' array.
                # In the event that we weren't storing data in an auxillary data structure,
                # We would need to create a boolean 'seen' array to ensure we don't revisit nodes
                if attributes.color == "white":
                    attributes.color = "gray"
                    attributes.distance = vertex_attributes[parent].distance + 1
                    attributes.parent = parent
                    q.append(adjacent_vertex)

            vertex_attributes[parent].color = "black"

    def standard_BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_graph()
    graph.BFS(0)
    graph.standard_BFS(0)