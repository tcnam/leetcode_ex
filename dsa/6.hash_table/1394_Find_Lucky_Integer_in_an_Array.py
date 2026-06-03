import typing as t

class Solution:
    def findLucky(self, arr: t.List[int]) -> int:
        freq_dict: t.Dict[int, int] = {}
        result: int = -1
        for ind in range(0, len(arr), 1):
            freq_dict[arr[ind]] = freq_dict.get(arr[ind], 0) + 1

        for key in freq_dict.keys():
            if key == freq_dict.get(key) and key > result:
                result = key
        
        return result
