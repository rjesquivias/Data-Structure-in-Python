import math
import sys

class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        segmentSize = (self.next_power_of_2(n) * 2) - 1
        self.segmentArray = [sys.maxsize for _ in range(segmentSize)]
        self.constructSumRangeTree(arr, 0, 0, n - 1)

    def next_power_of_2(self, x):
        return 1 if x == 0 else 2**math.ceil(math.log2(x))

    def constructMinRangeTree(self, arr, pos, low, high):
        # Leaf Node Condition
        if low == high:
            self.segmentArray[pos] = arr[low]
            return

        # If not at leaf node, we need to partition the array in half
        mid = low + (high - low) // 2
        left_child = 2 * pos + 1
        right_child = 2 * pos + 2

        # Recursively solve our current range by splitting it in half and passing it to the left and right
        # The only difference between this and a normal binary search algorithm is that we are also passing 
        # an index with us to the current segmentTree location we are currently trying to solve
        self.constructMinRangeTree(arr, left_child, low, mid)
        self.constructMinRangeTree(arr, right_child, mid + 1, high)

        # Think of this like post order, we can construct the left and right subtree partitions
        # and then solve for our current index position which stores the solution to the current range(low - high)
        self.segmentArray[pos] = min(self.segmentArray[left_child], self.segmentArray[right_child])

    def constructSumRangeTree(self, arr, pos, low, high):
        # Leaf Node Condition
        if low == high:
            self.segmentArray[pos] = arr[low]
            return

        # If not at leaf node, we need to partition the array in half
        mid = low + (high - low) // 2
        left_child = 2 * pos + 1
        right_child = 2 * pos + 2

        # Recursively solve our current range by splitting it in half and passing it to the left and right
        # The only difference between this and a normal binary search algorithm is that we are also passing 
        # an index with us to the current segmentTree location we are currently trying to solve
        self.constructSumRangeTree(arr, left_child, low, mid)
        self.constructSumRangeTree(arr, right_child, mid + 1, high)

        # Think of this like post order, we can construct the left and right subtree partitions
        # and then solve for our current index position which stores the solution to the current range(low - high)
        self.segmentArray[pos] = self.segmentArray[left_child] + self.segmentArray[right_child]

    def __str__(self):
        sol = []
        for x in self.segmentArray:
            sol.append(x)
        return str(sol)

if __name__ == "__main__":
    arr = [-1, 2, 4, 0]
    segmentTree = SegmentTree(arr)
    print(segmentTree)
