from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'B', 'E'],
    'E': ['B', 'D'],
}

# set: A B C D E
# queue:

def bfs(graph, start_node):
  visited = set()
  queue = deque([start_node])

  while queue:
    node = queue.popleft()
    if node not in visited:
      print(node, end=' ')
      visited.add(node)

      for neighbor in graph[node]:
        if neighbor not in visited:
          queue.append(neighbor)

bfs(graph, 'A')