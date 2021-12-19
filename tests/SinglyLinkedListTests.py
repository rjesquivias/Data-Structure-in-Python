import unittest
from core.SinglyLinkedList import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def test_is_empty(self):
        l = SinglyLinkedList()
        self.assertTrue(l.is_empty(), "List is not empty")

    def test_add(self):
        l = SinglyLinkedList()
        l.add(5)
        self.assertEqual(l.head.data, 5)
        l.add(12)
        self.assertEqual(l.head.data, 12)

    def test_size(self):
        l = SinglyLinkedList()
        self.assertEqual(l.size(), 0)
        l.add(1)
        self.assertEqual(l.size(), 1)
        l.add(2)
        self.assertEqual(l.size(), 2)
        l.add(3)
        self.assertEqual(l.size(), 3)
        l.pop()
        l.pop()
        self.assertEqual(l.size(), 1)

    def test_search(self):
        l = SinglyLinkedList()
        l.add(8)
        l.add(2)
        l.add(12)
        l.add(3)
        l.add(44)
        l.add(23)

        self.assertTrue(l.search(2), "Item not found in the list.")
        self.assertFalse(l.search(9), "Item found in the list.")

    def test_remove(self):
        l = SinglyLinkedList()
        l.add(8)
        l.add(2)
        l.add(12)
        l.add(3)
        l.add(44)
        l.add(23)

        self.assertTrue(l.search(2), "Item not found in the list.")
        l.remove(2)
        self.assertFalse(l.search(2), "Item found in the list.")

        self.assertRaises(ValueError, l.remove, 9)

    def test_append(self):
        l = SinglyLinkedList()
        l.add(8)
        l.add(2)
        l.add(12)
        l.add(3)
        l.add(44)
        l.add(23)
        self.assertTrue(l.index(23) == 0, "Item is at the wrong index.")
        l.append(15)
        self.assertTrue(l.index(23) == 0, "Item is at the wrong index.")
        self.assertTrue(l.index(15) == 6, "Item is at the wrong index.")

    def test_index(self):
        l = SinglyLinkedList()
        l.add(8)
        l.add(2)
        l.add(12)
        l.add(3)
        l.add(44)
        l.add(23)

        self.assertTrue(l.index(23) == 0, "Item is at the wrong index.")
        self.assertTrue(l.index(44) == 1, "Item is at the wrong index.")
        self.assertTrue(l.index(3) == 2, "Item is at the wrong index.")
        self.assertTrue(l.index(12) == 3, "Item is at the wrong index.")
        self.assertTrue(l.index(2) == 4, "Item is at the wrong index.")
        self.assertTrue(l.index(8) == 5, "Item is at the wrong index.")

        self.assertRaises(ValueError, l.index, 9)

    def test_insert(self):
        l = SinglyLinkedList()
        l.add(8)
        l.add(2)
        l.add(12)
        l.add(3)
        l.add(44)
        l.add(23)

        l.insert(0, 99)
        self.assertTrue(l.index(99) == 0, "Item is at the wrong index.")
        self.assertTrue(l.index(23) == 1, "Item is at the wrong index.")

        l.insert(7, 100)
        self.assertTrue(l.index(100) == 7, "Item is at the wrong index.")
        self.assertTrue(l.index(8) == 6, "Item is at the wrong index.")

        l.insert(3, 101)
        self.assertTrue(l.index(101) == 3, "Item is at the wrong index.")
        self.assertTrue(l.index(3) == 4, "Item is at the wrong index.")

    def test_pop(self):
        l = SinglyLinkedList()
        l.add(8)
        l.add(2)
        l.add(12)
        l.add(3)
        l.add(44)
        l.add(23)

        self.assertTrue(l.pop() == 8, "The wrong item was popped.")
        self.assertTrue(l.pop() == 2, "The wrong item was popped.")
        self.assertTrue(l.pop() == 12, "The wrong item was popped.")
        self.assertTrue(l.pop() == 3, "The wrong item was popped.")
        self.assertTrue(l.pop() == 44, "The wrong item was popped.")
        self.assertTrue(l.pop() == 23, "The wrong item was popped.")

        self.assertRaises(IndexError, l.pop)

    def test_pop_at_pos(self):
        l = SinglyLinkedList()
        l.add(8)
        l.add(2)
        l.add(12)
        l.add(3)
        l.add(44)
        l.add(23)

        self.assertTrue(l.pop_at_pos(0) == 23, "The wrong item was popped.")
        self.assertTrue(l.pop_at_pos(4) == 8, "The wrong item was popped.")
        self.assertTrue(l.pop_at_pos(1) == 3, "The wrong item was popped.")
        self.assertTrue(l.pop_at_pos(0) == 44, "The wrong item was popped.")
        self.assertTrue(l.pop_at_pos(0) == 12, "The wrong item was popped.")
        self.assertTrue(l.pop_at_pos(0) == 2, "The wrong item was popped.")
        
        self.assertRaises(IndexError, l.pop_at_pos, 0)

unittest.main()