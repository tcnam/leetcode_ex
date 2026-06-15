import typing as t

class Solution:
    def canVisitAllRooms(self, rooms: t.List[t.List[int]]) -> bool:
        stack: t.List[int] = [0]
        visited: t.Set[int] = set()
        while stack:
            cur: int = stack.pop()
            if cur in visited:
                continue
            
            visited.add(cur)
            for adj in rooms[cur]:
                if adj not in visited:
                    stack.append(adj)
        
        if len(visited) == len(rooms):
            return True
        else:
            return False