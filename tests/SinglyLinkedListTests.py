import unittest
from core.SinglyLinkedList import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def test_is_empty(self):
        l = SinglyLinkedList()
        self.assertTrue(l.is_empty(), "List is not empty")

unittest.main()