from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        track_ind: int = 0
        found_result: bool = False
        if track_ind >= len(strs[0]):
            return ""
        
        while track_ind < len(strs[0]):
            for ind in range(1, len(strs), 1):
                if (track_ind >= len(strs[ind])
                or strs[0][track_ind] != strs[ind][track_ind]):
                    found_result = True
                    break
            if found_result:
                break
            else:
                track_ind += 1
        
        return strs[0][0:track_ind]

        