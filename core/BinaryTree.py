class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def inorder(self):
        self._inorder(self.root)

    # A utility function to do inorder traversal of BST
    def _inorder(self, root):
        if root is not None:
            self._inorder(root.left)
            print root.key,
            self._inorder(root.right)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    # A utility function to insert a
    # new node with given key in BST
    def _insert(self, node, key):

        # If the tree is empty, return a new node
        if node is None:
            return Node(key)

        # Otherwise recur down the tree
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        # return the (unchanged) node pointer
        return node

    # Given a non-empty binary
    # search tree, return the node
    # with minimum key value
    # found in that tree. Note that the
    # entire tree does not need to be searched
    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current

    def deleteNode(self, key):
        self.root = self._deleteNode(self.root, key)

    # Given a binary search tree and a key, this function
    # delete the key and returns the new root
    def _deleteNode(self, root, key):

        # Base Case
        if root is None:
            return root

        # If the key to be deleted
        # is smaller than the root's
        # key then it lies in left subtree
        if key < root.key:
            root.left = self._deleteNode(root.left, key)

        # If the kye to be delete
        # is greater than the root's key
        # then it lies in right subtree
        elif(key > root.key):
            root.right = self._deleteNode(root.right, key)

        # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(root.right)

            # Copy the inorder successor's
            # content to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = self._deleteNode(root.right, temp.key)

        return root

if __name__ == "__main__":
    # Driver code
    """ Let us create following BST
                50
            /	 \
            30	 70
            / \ / \
        20 40 60 80 """

    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    print "Inorder traversal of the given tree"
    tree.inorder()

    print "\nDelete 20"
    tree.deleteNode(20)
    print "Inorder traversal of the modified tree"
    tree.inorder()

    print "\nDelete 30"
    tree.deleteNode(30)
    print "Inorder traversal of the modified tree"
    tree.inorder()

    print "\nDelete 50"
    tree.deleteNode(50)
    print "Inorder traversal of the modified tree"
    tree.inorder()
