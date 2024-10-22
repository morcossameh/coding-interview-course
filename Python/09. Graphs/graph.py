# 0   1
# | \ |
# 2   3


# Adjacency Matrix
#   0 1 2 3
# 0 0 0 1 1
# 1 0 0 0 1
# 2 1 0 0 0
# 3 1 1 0 0
# lookup O(1)
# space = O(V^2)

class GraphMatrix:
  def __init__(self, vertices_num):
    self.vertices_num = vertices_num
    self.matrix = [[0] * vertices_num for _ in range(vertices_num)]

  def add_edge(self, u, v, weight=1):
    self.matrix[u][v] = weight
    self.matrix[v][u] = weight # undirected

  def remove_edge(self, u, v):
    self.matrix[u][v] = 0
    self.matrix[v][u] = 0 # undirected

  def display(self):
    for row in self.matrix:
      print(row)

graph = GraphMatrix(4)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 3)
graph.display()

# 0   1
# | \ |
# 2   3

# Adjacency List
# 0: [2, 3]
# 2: [0]
# 3: [0, 1]
# 1: [3]
# space O(V+E)
# lookup O(V)

class GraphList:
  def __init__(self):
    self.adj_list = {}

  def add_vertex(self, v):
    if v not in self.adj_list:
      self.adj_list[v] = []

  def add_edge(self, u, v):
    self.add_vertex(u)
    self.add_vertex(v)
    self.adj_list[u].append(v)
    self.adj_list[v].append(u)

  def remove_edge(self, u, v):
    if u in self.adj_list and v in self.adj_list[u]:
      self.adj_list[u].remove(v)
    if v in self.adj_list and u in self.adj_list[v]:
      self.adj_list[v].remove(u)

  def display(self):
    for vertex in self.adj_list:
      print(f"{vertex}: {self.adj_list[vertex]}")

graph2 = GraphList()
graph2.add_edge(0, 2)
graph2.add_edge(0, 3)
graph2.add_edge(1, 3)
graph2.remove_edge(0, 2)
graph2.display()
