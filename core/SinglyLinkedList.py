class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
        return str(self._data)

class SinglyLinkedList:
    """A Singly Linked List Implementation"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """Tests to see if the list is empty"""
        return self.head == None

    def add(self, item):
        """Adds a new item to the list"""
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """Returns the number of items in the list"""
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        """Searches for an item in the list"""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        """Removes the item from the list"""
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("{} is not in the list".format(item))
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def append(self, item):
        """Adds a new item to the end of the list making it the last item in the collection"""
        temp = Node(item)
        
        if self.head is None:
            self.head = temp

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = temp

    def index(self, item):
        """Returns the position of item in the list. It needs the item and returns the index."""
        current = self.head
        count = 0
        while current is not None:
            if current.data == item:
                break
            count = count + 1
            current = current.next

        if current is None:
            raise ValueError("{} is not in the list".format(item))
        else:
            return count

    def insert(self, pos, item): 
        """Adds a new item to the list at position pos. It needs the item and returns nothing."""
        current = self.head
        previous = None

        while current is not None and pos > 0:
            previous = current
            current = current.next
            pos = pos - 1

        if pos > 0:
            raise IndexError("List index {} is out of range.".format(pos))
        else:
            temp = Node(item)
            if previous is None:
                temp.next = current
                self.head = temp
            else:
                temp.next = previous.next
                previous.next = temp

    def pop(self):
        """ removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item. """
        if self.head is None:
            raise IndexError("Pop from empty list")

        current = self.head
        previous = None
        while current.next is not None:
            previous = current
            current = current.next

        if previous is None:
            data = current.data
            self.head = None
            current = None
            return data
        else:
            data = current.data
            previous.next = current.next
            current = None
            return data

    def pop_at_pos(self, pos):
        """ removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list. """
        if self.head is None:
            raise IndexError("Pop from empty list")
        
        previous = None
        current = self.head
        while current.next is not None and pos > 0:
            previous = current
            current = current.next
            pos = pos - 1

        if pos > 0:
            raise IndexError("List index {} is out of range.".format(pos))
        else:
            if previous is None:
                data = current.data
                self.head = current.next
                current = None
                return data
            else:
                data = current.data
                previous.next = current.next
                current = None
                return data
