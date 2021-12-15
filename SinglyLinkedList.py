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
        
if __name__ == "__main__":
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.prepend("D")
    llist.insert_after_node(llist.head.next, "E")
    llist.print_list() 

    print("Deleting B and E")
    llist.delete_node("B")
    llist.delete_node("E")
    llist.delete_node_at_pos(0)
    llist.print_list() 

    print(llist.len_iterative())
    print(llist.len_recursive(llist.head))