# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert at end of the circular list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point to itself
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head  # Link back to head

    def display(self):
        """Display the circular list."""
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

# 🔎 Example usage
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert("Sun")
    cll.insert("Mon")
    cll.insert("Tue")
    cll.insert("Wed")

    cll.display()  # Sun -> Mon -> Tue -> Wed -> (back to head)
