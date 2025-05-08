# Define the graph as a dictionary
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2, 6],
    6: [5]
}

# DFS using recursion
def dfs(node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

# BFS using queue
from collections import deque

def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Run the traversals
print("DFS:")
dfs(0, set())

print("\nBFS:")
bfs(0)
