graph = {
    'A': ['B', 'C'],
    'B': ['A', 'E'],
    'C': ['A', 'B', 'D'],
    'D': ['E'],
    'E': ['D'],
}

def dfs(node, graph, visited):
  visited.add(node)

  print(node, end=' ')

  for neighbor in graph[node]:
    if neighbor not in visited:
      dfs(neighbor, graph, visited)

  
visited = set()
dfs('A', graph, visited)