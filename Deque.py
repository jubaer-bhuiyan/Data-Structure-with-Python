# deque.py

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def add_front(self, item):
        self.items.insert(0, item)  # Insert at the beginning

    def add_rear(self, item):
        self.items.append(item)  # Insert at the end

    def remove_front(self):
        if self.is_empty():
            return "Deque is empty"
        return self.items.pop(0)  # Remove from beginning

    def remove_rear(self):
        if self.is_empty():
            return "Deque is empty"
        return self.items.pop()  # Remove from end

    def peek_front(self):
        return self.items[0] if not self.is_empty() else None

    def peek_rear(self):
        return self.items[-1] if not self.is_empty() else None

    def size(self):
        return len(self.items)

    def display(self):
        print("Deque contents:", self.items)


# ✅ Example usage
if __name__ == "__main__":
    dq = Deque()
    dq.add_rear(10)
    dq.add_front(5)
    dq.add_rear(15)
    dq.display()
    print("Front:", dq.peek_front())
    print("Rear:", dq.peek_rear())
    dq.remove_front()
    dq.remove_rear()
    dq.display()
