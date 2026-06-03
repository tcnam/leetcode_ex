import typing as t

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set: t.Set[str] = set()
        result: int = 0
        for jew in jewels:
            if jew not in jewels_set:
                jewels_set.add(jew)
        
        for stone in stones:
            if stone in jewels_set:
                result += 1
        
        return result