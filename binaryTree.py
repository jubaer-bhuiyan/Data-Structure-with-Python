# Node class for Binary Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Tree class
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert value using BFS to keep tree balanced (for demo)."""
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def inorder(self, node):
        """Inorder traversal: Left ➝ Root ➝ Right"""
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

# 🔎 Example usage
if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(20)
    bt.insert(30)
    bt.insert(40)

    print("Inorder Traversal:")
    bt.inorder(bt.root)  # 40 20 10 30
