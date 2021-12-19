class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.header = Node()
        self.trailer = Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header

    def prepend(self, data):
        new_node = Node(data=data)
        nxt_node = self.header.next

        self.header.next = new_node

        new_node.prev = self.header
        new_node.next = nxt_node

        nxt_node.prev = new_node

    def append(self, data):
        new_node = Node(data=data)
        prev_node = self.trailer.prev

        prev_node.next = new_node

        new_node.prev = prev_node
        new_node.next = self.trailer

        self.trailer.prev = new_node

    def insertAfter(self, prev_node, data):
        if prev_node is None or prev_node is self.trailer:
            return

        new_node = Node(data=data)
        next_node = prev_node.next

        prev_node.next = new_node

        new_node.prev = prev_node
        new_node.next = next_node

        next_node.prev = new_node
        

    def insertBefore(self, next_node, data):
        if next_node is None or next_node is self.header
            return

        new_node = Node(data=data)
        prev_node = next_node.prev

        prev_node.next = new_node

        new_node.prev = prev_node
        new_node.next = next_node

        next_node.prev = new_node