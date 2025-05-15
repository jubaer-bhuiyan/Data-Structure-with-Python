from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Add edge from u to v (directed)."""
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(self.graph[vertex])
        return result

    def dfs(self, start, visited=None, result=None):
        if visited is None:
            visited = set()
        if result is None:
            result = []

        visited.add(start)
        result.append(start)
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, result)
        return result

    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")


# ✅ Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Graph Structure:")
    g.display()

    print("\nBFS starting from 2:", g.bfs(2))
    print("DFS starting from 2:", g.dfs(2))
