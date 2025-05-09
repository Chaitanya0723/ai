from collections import deque

# Accept user input for the graph
graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

# Recursive DFS
def dfs(v, visited=set()):
    if v in visited: return
    print(v, end=' ')
    visited.add(v)
    for n in graph.get(v, []):
        dfs(n, visited)

# Recursive BFS
def bfs(queue, visited=set()):
    if not queue: return
    v = queue.popleft()
    if v in visited:
        return bfs(queue, visited)
    print(v, end=' ')
    visited.add(v)
    queue.extend(n for n in graph.get(v, []) if n not in visited)
    bfs(queue, visited)

# Take starting node input
start = input("Enter starting node: ")

print("\nDFS:")
dfs(start)

print("\nBFS:")
bfs(deque([start]))
