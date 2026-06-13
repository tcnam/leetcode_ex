import typing as t
from collections import deque


class Solution:
    def validPath(self, n: int, edges: t.List[t.List[int]], source: int, destination: int) -> bool:
        adj_matrix: t.Dict[int, t.List[int]] = self.buildAdjMatrix(edges)
        queue: deque = deque([source])
        visited: t.Set[int] = set()
        while queue:
            cur_vertex: int = queue.popleft()
            if cur_vertex in visited:
                continue

            if cur_vertex == destination:
                return True

            visited.add(cur_vertex)

            for adj_vertex in adj_matrix.get(cur_vertex):
                if adj_vertex in visited:
                    continue
                queue.append(adj_vertex)
            
            visited.add(cur_vertex)
        
        return False
    
    def buildAdjMatrix(self, edges: t.List[t.List[int]]) -> t.Dict[int, t.List[int]]:
        adj_matrix: t.Dict[int, t.List[int]] = {}
        for ind in range(0, len(edges), 1):
            first_vertex: int = edges[ind][0]
            second_vertex: int = edges[ind][1]

            if first_vertex not in adj_matrix.keys():
                adj_matrix[first_vertex] = []
            
            if second_vertex not in adj_matrix.keys():
                adj_matrix[second_vertex] = []
            
            adj_matrix[first_vertex].append(second_vertex)
            adj_matrix[second_vertex].append(first_vertex)
        
        return adj_matrix