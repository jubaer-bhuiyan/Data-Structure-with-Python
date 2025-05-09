class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Chaining for collisions

    def _hash(self, key):
        """Basic hash function using built-in hash() and modulo."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert or update key-value pair."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update
                return
        self.table[index].append([key, value])

    def get(self, key):
        """Retrieve value for a key."""
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        """Remove key-value pair."""
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")

# 🔎 Example usage
if __name__ == "__main__":
    ht = HashTable()

    ht.insert("apple", 5)
    ht.insert("banana", 10)
    ht.insert("orange", 3)

    print("Hash Table:")
    ht.display()

    print("\nGet value for 'banana':", ht.get("banana"))  # 10

    ht.delete("banana")
    print("\nAfter deleting 'banana':")
    ht.display()