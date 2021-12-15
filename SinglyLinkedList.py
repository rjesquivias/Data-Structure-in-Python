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

        
if __name__ == "__main__":
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")

    llist.prepend("D")

    llist.insert_after_node(llist.head.next, "E")

    llist.print_list() 