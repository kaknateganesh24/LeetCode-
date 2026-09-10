class Solution(object):
    def validPath(self, n, edges, source, destination):
        graph = {}
        for i in range(n):
            graph[i] = []
        for edge in edges:
            a = edge[0]
            b = edge[1]
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        self.dfs(graph, source, visited)
        
        return destination in visited
    
    def dfs(self, graph, node, visited):
        if node in visited:
            return
        visited.add(node)
        for neighbour in graph[node]:
            self.dfs(graph, neighbour, visited)