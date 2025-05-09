graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F',],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Recursive DFS
def dfs(v, visited=set()):
    if v in visited:
        return
    print(v, end=' ')
    visited.add(v)
    for n in graph[v]:
        dfs(n, visited)

# Recursive BFS
from collections import deque
def bfs(queue, visited=set()):
    if not queue:
        return
    v = queue.popleft()
    if v in visited:
        return bfs(queue, visited)
    print(v, end=' ')
    visited.add(v)
    queue.extend(n for n in graph[v] if n not in visited)
    bfs(queue, visited)

# Run both
print("DFS:")
dfs('A')
print("\nBFS:")
bfs(deque(['A']))
