import typing as t


class Solution:
    def findCircleNum(self, isConnected: t.List[t.List[int]]) -> int:
        stack: t.List[int] = []
        visited: t.Set[int] = set()
        result: int = 0

        for ind in range(0, len(isConnected), 1):
            if ind in visited:
                continue
            stack.append(ind)
            while stack:
                cur_city: int = stack.pop()
                visited.add(cur_city)
                for adj_ind in range(0, len(isConnected[cur_city]), 1):
                    if (
                        adj_ind not in visited
                        and isConnected[cur_city][adj_ind] == 1 
                    ):
                        stack.append(adj_ind)
            result += 1
        
        return result
    