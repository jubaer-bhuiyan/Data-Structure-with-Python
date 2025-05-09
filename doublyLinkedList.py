# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Link to previous node
        self.next = None  # Link to next node

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert at the end."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display_forward(self):
        """Print from head to tail."""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            last = current  # Save last node for backward traversal
            current = current.next
        print("None")

    def display_backward(self):
        """Print from tail to head."""
        current = self.head
        if not current:
            print("List is empty")
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# 🔎 Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert("A")
    dll.insert("B")
    dll.insert("C")

    print("Forward:")
    dll.display_forward()   # A <-> B <-> C <-> None

    print("Backward:")
    dll.display_backward()  # C <-> B <-> A <-> None
