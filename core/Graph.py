from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def addEdge(self, v, w, cost=0):
        self.adj[v].append((w, cost))
        if len(self.adj[w]) == 0:
            self.adj[w] = []

    def printGraph(self):
        for key, li in self.adj.items():
            print(key, end=": ")
            print(li)

    # O(V + E) time complexity
    # O(V) auxillary space on the stack
    def topologicalSort(self):
        stack = []
        visited = set()

        for vertex, neighbors in self.adj.items():
            if vertex not in visited:
                self.topologicalSortUtil(vertex, stack, visited)

        return stack[::-1]

    def topologicalSortUtil(self, vertex, stack, visited):
        visited.add(vertex)

        for neighbor in self.adj[vertex]:
            if neighbor[0] not in visited:
                self.topologicalSortUtil(neighbor[0], stack, visited)

        stack.append(vertex)

    # O(E + VLogV) or O(V^2)
    def dijkstra(self, src):
        # Create a dictionary for distances
        # and set every key's distance to inf
        distances = {}
        for key in self.adj.keys():
            distances[key] = float("inf")

        # Set source key distance to 0
        distances[src] = 0

        # Create a pq initialized with src
        min_distances = [(0, src)]
        visited = set()

        while min_distances:
            # Visit the current minimum if we haven't already visited it
            cost, cur = heapq.heappop(min_distances)
            if cur in visited: continue
            visited.add(cur)

            # Relax all neighbors edges
            for neighbor in self.adj[cur]:
                if neighbor in visited: continue
                this_dist = cost + neighbor[1]
                # If we found a new minimum, update the distance and add the new 
                # value to the heap
                # Duplicates are handled via a visited array
                if this_dist < distances[neighbor[0]]:
                    distances[neighbor[0]] = this_dist
                    heapq.heappush(min_distances, (this_dist, neighbor[0]))

        #if len(visited) != len(self.adj.keys()): return -1
        return distances

if __name__ == "__main__":
    g = Graph()
    g.addEdge(5, 2, 5)
    g.addEdge(5, 0, 3)
    g.addEdge(4, 0, 9)
    g.addEdge(4, 1, 2)
    g.addEdge(2, 3, 4)
    g.addEdge(3, 1, 5)
    g.printGraph()
    print(g.topologicalSort())
    print(g.dijkstra(5))