class Graph:
    def __init__(self, g_dict):
        if g_dict is None:
            g_dict = {}
        self.g_dict = g_dict

    def add_node(self, node):
        self.g_dict[node] = []

    def add_edge(self, node, edge):
        self.g_dict[node].append(edge)

    def bfs(self, node):
        visited = [node]
        queue = [node]
        while queue:
            de_node = queue.pop(0)
            print(de_node)
            for ed in self.g_dict[de_node]:
                if ed not in visited:
                    visited.append(ed)
                    queue.append(ed)

    def dfs(self, node):
        visited = [node]
        stack = [node]
        while stack:
            pop_node = stack.pop()
            print(pop_node)
            for ed in self.g_dict[pop_node]:
                if ed not in visited:
                    visited.append(ed)
                    stack.append(ed)


graph_dict = {'A': ['B', 'C', 'D'], 'B': ['A', 'D', 'E'], 'C': [
    'A', 'D'], 'D': ['C', 'A', 'B', 'E'], 'E': ['B', 'D']}


graph = Graph(graph_dict)
graph.dfs('A')
