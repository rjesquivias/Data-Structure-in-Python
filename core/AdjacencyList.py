from collections import defaultdict
from collections import deque
import sys

# Adjacency List representation in Python
class VertexAttributes:
    def __init__(self, color="white", distance=sys.maxsize, parent=None, discovery_time=None, finishing_time=None):
        self.color = color
        self.distance = distance
        self.parent = parent
        # Below times used in DFS (refer to CLRS)
        self.discovery_time = discovery_time
        self.finishing_time = finishing_time

    def __str__(self):
        return str("color: " + str(self.color) + " | distance: " + str(self.distance) + " | parent: " + str(self.parent) + "| discovery time: " + str(self.discovery_time) + "| finishing time: " + str(self.finishing_time))

class Graph:
    def __init__(self, vertex_attributes=None):
        self.graph = defaultdict(list)
        self.vertex_attributes = vertex_attributes

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
    # O(V + E)
    def BFS(self, source):
        # Initialize our auxillary data structures for each vertex
        self.vertex_attributes = defaultdict(VertexAttributes)

        for vertex in self.graph:
            # Create our VertexAttribute object
            vertex_attribute = VertexAttributes()
            vertex_attribute.color = "white"
            vertex_attribute.distance = sys.maxsize
            vertex_attribute.parent = None
            # Store the data using the vertices index value as a key
            self.vertex_attributes[vertex] = vertex_attribute

        # Source vertex data initialization
        self.vertex_attributes[source].color = "gray"
        self.vertex_attributes[source].distance = 0

        # Standard BFS
        q = deque()
        q.append(source)
        while len(q) != 0:
            parent = q.popleft()
            print(str(parent), end=" ")
            print(self.vertex_attributes[parent])
            for adjacent_vertex in self.graph[parent]:
                attributes = self.vertex_attributes[adjacent_vertex]
                # We are using the color attribute as a replacement for a 'seen' array.
                # In the event that we weren't storing data in an auxillary data structure,
                # We would need to create a boolean 'seen' array to ensure we don't revisit nodes
                if attributes.color == "white":
                    attributes.color = "gray"
                    attributes.distance = self.vertex_attributes[parent].distance + 1
                    attributes.parent = parent
                    q.append(adjacent_vertex)

            self.vertex_attributes[parent].color = "black"

    # O(V + E)
    def standard_BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = defaultdict(bool)
 
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

    # O(n) where n = number of nodes in path from source to destination
    def print_path(self, source, destination):
        if self.vertex_attributes is None:
            print(f"Run BFS from source {source} first to calculate the path")
            return

        if destination == source:
            print(source)
        elif self.vertex_attributes[destination].parent == None:
            print(f"No path from {source} to {destination} exists.")
        else:
            self.print_path(source, self.vertex_attributes[destination].parent)
            print(destination)

    # O(V + E)
    def DFS(self):
         # Initialize our auxillary data structures for each vertex
        self.vertex_attributes = defaultdict(VertexAttributes)

        for vertex in self.graph:
            # Create our VertexAttribute object
            vertex_attribute = VertexAttributes()
            vertex_attribute.color = "white"
            vertex_attribute.parent = None
            # Store the data using the vertices index value as a key
            self.vertex_attributes[vertex] = vertex_attribute

        self.time = 0
        for vertex in self.graph:
            if self.vertex_attributes[vertex].color == "white":
                self.DFS_visit(vertex)

    def DFS_visit(self, current_vertex):
        self.time += 1
        self.vertex_attributes[current_vertex].discovery_time = self.time
        self.vertex_attributes[current_vertex].color = "gray"
        for vertex in self.graph[current_vertex]:
            if self.vertex_attributes[vertex].color == "white":
                self.vertex_attributes[vertex].parent = current_vertex
                self.DFS_visit(vertex)
        self.vertex_attributes[current_vertex].color = "black"
        self.time += 1
        self.vertex_attributes[current_vertex].finishing_time = self.time

        print(current_vertex, end=" ")
        print(self.vertex_attributes[current_vertex])

if __name__ == "__main__":
    # Create graph and edges
    graph = Graph()

    graph.add_edge('v', 'r')
    graph.add_edge('r', 's')
    graph.add_edge('s', 'w')
    graph.add_edge('w', 't')
    graph.add_edge('w', 'x')
    graph.add_edge('t', 'u')
    graph.add_edge('t', 'x')
    graph.add_edge('x', 'u')
    graph.add_edge('x', 'y')
    graph.add_edge('u', 'y')

    graph.print_graph()
    graph.BFS('s')
    graph.standard_BFS('s')
    print()
    graph.print_path('s', 'y')

    graph.DFS()