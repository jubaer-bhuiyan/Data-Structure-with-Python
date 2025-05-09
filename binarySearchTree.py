# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BST class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert value recursively."""
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        return node

    def inorder(self, node):
        """Inorder Traversal: Left -> Root -> Right"""
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def search(self, value):
        """Search for a value in BST."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

# 🔎 Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("Inorder Traversal (Sorted):")
    bst.inorder(bst.root)  # 20 30 40 50 60 70 80

    # Search
    result = bst.search(60)
    print("\n\nSearch for 60:", "Found" if result else "Not Found")
