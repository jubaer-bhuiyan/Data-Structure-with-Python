from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # adjacency list

    def add_edge(self, u, v):
        self.graph[u].append(v)
        # Uncomment below for undirected graph:
        # self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        print("BFS Traversal:")
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend([neigh for neigh in self.graph[vertex] if neigh not in visited])
        print()

    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        for neigh in self.graph[vertex]:
            if neigh not in visited:
                self.dfs_util(neigh, visited)

    def dfs(self, start):
        visited = set()
        print("DFS Traversal:")
        self.dfs_util(start, visited)
        print()


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.bfs(2)
    g.dfs(2)
