import typing as t

class Solution:
    def isBipartite(self, graph: t.List[t.List[int]]) -> bool:
        visited: t.List[int] = [0] * len(graph)
        set_ind: int = 1
        result: bool = True
        for ind in range(0, len(graph), 1):
            if visited[ind] != 0 or len(graph[ind]) == 0:
                continue
            next_result: bool = self.dfs(graph, ind, set_ind, visited)
            result = result & next_result
        return result
    
    def dfs(self, graph: t.List[t.List[int]], ind: int, set_ind: int, visited: t.List[int]) -> bool:
        visited[ind] = set_ind
        next_set_ind = 1 if set_ind == 2 else 2
        for adj_node in graph[ind]:
            if visited[adj_node] == 0:
                if not self.dfs(graph, adj_node, next_set_ind, visited):
                    return False
            else:
                if next_set_ind != visited[adj_node]:
                    return False
        return True