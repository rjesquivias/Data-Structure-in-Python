class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        iter_node = self.head
        while iter_node.next is not None:
            iter_node = iter_node.next

        iter_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0
            while cur_node and count < pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next

        return count

    def len_recursive(self, node):
        if node is None:
            return 0

        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        cur_1 = self.head
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        prev_2 = None
        cur_2 = self.head
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next

        if not cur_1 or not cur_2:
            return

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1

        cur_1.next, cur_2.next = cur_2.next, cur_1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            return _reverse_recursive(nxt, cur)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        sentinal = Node(-1)
        s_iter = sentinal

        if not p:
            self.head = q
            return q
        if not q:
            self.head = p
            return p

        while p and q:
            if p.data <= q.data:
                s_iter.next = p
                s_iter = s_iter.next
                p = p.next
            else:
                s_iter.next = q
                s_iter = s_iter.next
                q = q.next

        if not p:
            s_iter.next = q
        if not q:
            s_iter.next = p

        self.head = sentinal.next

    def remove_duplicates(self):
        cur = self.head
        prev = None
        seen = set()

        while cur:
            if cur.data in seen:
                prev.next = cur.next
                cur = None
            else:
                seen.add(cur.data)
                prev = cur
            cur = prev.next
        
if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(6)
    llist.append(1)
    llist.append(4)
    llist.append(2)
    llist.append(2)
    llist.append(4)

    print("Original Linked List")
    llist.print_list()
    print("Linked List After Removing Duplicates")
    llist.remove_duplicates()
    llist.print_list()