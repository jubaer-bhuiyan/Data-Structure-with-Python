# Node class
class Node:
    def __init__(self, data):
        self.data = data  # store data
        self.next = None  # store reference to next node

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # initially empty

    def insert(self, data):
        """Insert a new node at the end."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:  # traverse to last node
                current = current.next
            current.next = new_node

    def display(self):
        """Print all the elements in the list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# 🔎 Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert("apple")
    ll.insert("banana")
    ll.insert("cherry")

    print("Linked List:")
    ll.display()  # apple -> banana -> cherry -> None
