# segmentTree.py

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, idx, val, node, start, end):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(idx, val, 2 * node + 1, start, mid)
            else:
                self.update(idx, val, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, l, r, node, start, end):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left = self.query(l, r, 2 * node + 1, start, mid)
        right = self.query(l, r, 2 * node + 2, mid + 1, end)
        return left + right


# ✅ Example usage
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(arr)

    print("Range sum (1,3):", seg_tree.query(1, 3, 0, 0, len(arr) - 1))
    seg_tree.update(1, 10, 0, 0, len(arr) - 1)
    print("After update, range sum (1,3):", seg_tree.query(1, 3, 0, 0, len(arr) - 1))
