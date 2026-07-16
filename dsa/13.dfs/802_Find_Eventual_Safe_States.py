import typing as t

class Solution:
    def eventualSafeNodes(self, graph: t.List[t.List[int]]) -> t.List[int]:
        visited: t.List[bool] = [False] * len(graph)
        path: t.List[bool] = [False] * len(graph)

        for ind in range(0, len(graph), 1):
            if visited[ind]:
                continue 
            self.dfs(graph, ind, visited, path)

        return [ind for ind in range(0, len(path), 1) if not path[ind]]

    def dfs(self,
            graph: t.List[t.List[int]], 
            cur_node: int, 
            visited: t.List[bool], 
            path: t.List[bool]) -> bool:
        
        visited[cur_node] = True
        path[cur_node] = True

        for adj_node in graph[cur_node]:
            if not visited[adj_node]:
                if not self.dfs(graph, adj_node, visited, path):
                    return False

            if path[adj_node]:
                return False
        
        path[cur_node] = False
        return True
