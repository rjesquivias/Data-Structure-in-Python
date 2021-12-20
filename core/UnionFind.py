# A class to represent a disjoint set
# Runtime analysis: 
# without anything: 𝑂(𝑁)
# with Union by Rank: 𝑂(log𝑁)
# with Path Compression: 𝑂(𝛼(𝑁)) which is inverse Ackermann function.
class DisjointSet:
    parent = {}
 
    # stores the depth of trees
    rank = {}
 
    # perform MakeSet operation
    def makeSet(self, universe):
        # create `n` disjoint sets (one for each item)
        for i in universe:
            self.parent[i] = i
            self.rank[i] = 0
 
    # Find the root of the set in which element `k` belongs
    def Find(self, k):
        # if `k` is not the root
        if self.parent[k] != k:
            # path compression
            self.parent[k] = self.Find(self.parent[k])
        return self.parent[k]
 
    # Perform Union of two subsets
    def Union(self, a, b):
        # find the root of the sets in which elements `x` and `y` belongs
        x = self.Find(a)
        y = self.Find(b)
 
        # if `x` and `y` are present in the same set
        if x == y:
            return
 
        # Always attach a smaller depth tree under the root of the deeper tree.
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] = self.rank[y] + 1
 
 
def printSets(universe, ds):
    print([ds.Find(i) for i in universe])
 
 
if __name__ == '__main__':
 
    # universe of items
    universe = [1, 2, 3, 4, 5]
 
    # initialize `DisjointSet` class
    ds = DisjointSet()
 
    # create a singleton set for each element of the universe
    ds.makeSet(universe)
    printSets(universe, ds)
 
    ds.Union(4, 3)        # 4 and 3 are in the same set
    printSets(universe, ds)
 
    ds.Union(2, 1)        # 1 and 2 are in the same set
    printSets(universe, ds)
 
    ds.Union(1, 3)        # 1, 2, 3, 4 are in the same set
    printSets(universe, ds)