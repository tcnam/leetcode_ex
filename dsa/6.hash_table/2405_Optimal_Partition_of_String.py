import typing as t

class Solution:
    def partitionString(self, s: str) -> int:
        track_char_set: t.Set[str] = set()
        result: int = 0
        for ind in range(0, len(s), 1):
            if s[ind] in track_char_set:
                track_char_set.clear()
                result += 1
            track_char_set.add(s[ind])
        return result + 1