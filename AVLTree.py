class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get balance factor
        balance = self.get_balance(root)

        # Balance the tree
        # Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        # Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def pre_order(self, root):
        if root:
            print(root.key, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)


# Example usage
if __name__ == "__main__":
    avl = AVLTree()
    root = None

    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = avl.insert(root, key)

    print("Preorder Traversal of AVL Tree:")
    avl.pre_order(root)
