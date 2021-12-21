import math
import sys

# The number of leaf nodes = N (this corresponds to the original array)
# The number of internal nodes = N - 1 (Because it is a Full Binary Tree)
# The total number of nodes = 2N - 1
#
# Space required in a segment tree is the smallest power of 2 >= 2N - 1
# because elements are not filled adjacently but in powers of 2 (2i + 1, 2i + 2),
# and the last level can have varying spaces (its not a Complete Binary Tree)
#
# Height of segment tree is ceil(log2(N + 1))
# Size of segment array is 2^h - 1

# This data structure is only useful if updates are frequent.
# If updates are not frequent, it is quicker to use a sum_array where
# where sum_array[i] is the sum of the range 0-i. You can use this data structure 
# to query in constant time compared to LogN time. This data structure is only inefficient 
# when we have many update operations, since an update is linear. In that case, a segment trees
# LogN update time is more preferred even with the move to LogN query time from constant
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        # This can be replaced with n * 2
        segmentSize = (self.next_power_of_2(self.n) * 2) - 1
        self.original_array = arr
        self.segmentArray = [sys.maxsize for _ in range(segmentSize)]
        self.constructSumRangeTree(arr, 0, 0, self.n - 1)

    def next_power_of_2(self, x):
        return 1 if x == 0 else 2**math.ceil(math.log2(x))

    def constructMinRangeTree(self, arr, pos, left, right):
        # Leaf Node Condition
        if left == right:
            self.segmentArray[pos] = arr[left]
            return

        # If not at leaf node, we need to partition the array in half
        mid = left + (right - left) // 2
        left_child = 2 * pos + 1
        right_child = 2 * pos + 2

        # Recursively solve our current range by splitting it in half and passing it to the left and right
        # The only difference between this and a normal binary search algorithm is that we are also passing 
        # an index with us to the current segmentTree location we are currently trying to solve
        self.constructMinRangeTree(arr, left_child, left, mid)
        self.constructMinRangeTree(arr, right_child, mid + 1, right)

        # Think of this like post order, we can construct the left and right subtree partitions
        # and then solve for our current index position which stores the solution to the current range(left - right)
        self.segmentArray[pos] = min(self.segmentArray[left_child], self.segmentArray[right_child])

    # O(N)
    def constructSumRangeTree(self, arr, pos, left, right):
        # Leaf Node Condition
        if left == right:
            self.segmentArray[pos] = arr[left]
            return

        # If not at leaf node, we need to partition the array in half
        mid = left + (right - left) // 2
        left_child = 2 * pos + 1
        right_child = 2 * pos + 2

        # Recursively solve our current range by splitting it in half and passing it to the left and right
        # The only difference between this and a normal binary search algorithm is that we are also passing 
        # an index with us to the current segmentTree location we are currently trying to solve
        self.constructSumRangeTree(arr, left_child, left, mid)
        self.constructSumRangeTree(arr, right_child, mid + 1, right)

        # Think of this like post order, we can construct the left and right subtree partitions
        # and then solve for our current index position which stores the solution to the current range(left - right)
        self.segmentArray[pos] = self.segmentArray[left_child] + self.segmentArray[right_child]

    """
    pos: the current index
    left, right: the range that is stored at the current index
    query_left, query_right: the range that we are querying for
    """
    # O(LogN)
    def get_sum_in_range(self, pos, left, right, query_left, query_right):
        # There are 3 cases to handle for the (left, right) & (query_left, query_right) ranges
        # It's important to think of these from the perspective of the query range, not the current positions range
        # 1. Total overlap 
        # e.g. left = 2, right = 2, query_left = 2, query_right = 4
        # [2, 2] is totally overlapped by [2, 4]
        if query_left <= left and query_right >= right:
            return self.segmentArray[pos]
        # 2. No overlap
        if right < query_left or left > query_right:
            return 0
        # 3. Partial overlap
        # e.g. left = 0, right = 5, query_left = 2, query_right = 4
        # [0, 5] is partially overlapped by [2, 4]
        mid = left + (right - left) // 2
        left_child = 2 * pos + 1
        right_child = 2 * pos + 2

        return self.get_sum_in_range(left_child, left, mid, query_left, query_right) + \
               self.get_sum_in_range(right_child, mid + 1, right, query_left, query_right)

    # O(LogN)
    def update(self, update_pos, new_val):
        # Update our original array and calculate the difference between the old and new value
        diff = new_val - self.original_array[update_pos]
        self.original_array[update_pos] = new_val

        # Use the difference to updated only those nodes affected in our tree
        self._update(0, 0, self.n - 1, update_pos, diff)

    def _update(self, pos, left, right, update_pos, update_diff):
        # We need to update the values at each node affected by the update.
        # Affected nodes are nodes where the update_pos is within the range that node covers
        if left > update_pos or right < update_pos:
            return

        # Update our current node with our precalculated difference
        self.segmentArray[pos] += update_diff

        # If not at a leaf update the children
        if left != right:
            mid = left + (right - left) // 2
            left_child = 2 * pos + 1
            right_child = 2 * pos + 2

            self._update(left_child, left, mid, update_pos, update_diff)
            self._update(right_child, mid + 1, right, update_pos, update_diff)
        
    def __str__(self):
        sol = []
        for x in self.segmentArray:
            sol.append(x)
        return str(sol)

if __name__ == "__main__":
    arr = [1,2,5,6,7,9]
    segmentTree = SegmentTree(arr)
    print(segmentTree)
    segmentTree.update(3, 14)
    print(segmentTree)
    print(segmentTree.get_sum_in_range(0, 0, len(arr) - 1, 0, 6))
