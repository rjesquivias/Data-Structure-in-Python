class TrieNode:
    def __init__(self, terminal=False):
        self.terminal = terminal
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        temp = self.root
        for c in s:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]

        temp.terminal = True

    def search(self, s):
        temp = self.root
        for c in s:
            if temp is None or c not in temp.children:
                return False
            temp = temp.children[c]

        return temp.terminal if temp is not None else False

    def delete(self, s):
        self._delete(s, 0, self.root)

    def _delete(self, s, index, root):
        if root is None:
            return root

        if index >= len(s):
            root.terminal = False

            if self._has_no_children(root):
                root = None
        else:
            current_char = s[index]
            root.children[current_char] = self._delete(s, index + 1, root.children[current_char])

            if self._has_no_children(root) and root.terminal is False:
                root = None

        return root

    def _has_no_children(self, root):
        if root is None: 
            return False

        return len(root.children) == 0

    def __str__(self):
        stringList = []
        self._buildStringList(self.root, stringList)
        return str(stringList)

    def _buildStringList(self, root, stringList, currentString = ""):
        if root is None:
            return

        if root.terminal is True:
            stringList.append(currentString)

        for key, value in root.children.items():
            self._buildStringList(value, stringList, currentString + key)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("Hello")
    trie.insert("World")
    trie.insert("Another")
    trie.insert("Way")
    trie.insert("to")
    trie.insert("phone")
    trie.insert("pillow")
    trie.insert("pills")
    trie.insert("piller")

    print(trie)
    print(trie.search("pillow"))
    trie.delete("pillow")
    print(trie.search("pills"))
    print(trie.search("piller"))
    trie.delete("pills")
    print(trie.search("pills"))
    print(trie.search("piller"))
    trie.delete("piller")
    print(trie.search("pills"))
    print(trie.search("piller"))