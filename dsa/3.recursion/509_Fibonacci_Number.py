import typing as t

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        fib_dict: t.Dict[int, int] = {}
        return self._fibHelper(n-1, fib_dict) + self._fibHelper(n-2, fib_dict)
    
    def _fibHelper(self, n: int, fib_dict: t.Dict[int, int]):
        if n == 0 or n == 1:
            return n
    
        if n in fib_dict.keys():
            return fib_dict.get(n)

        fib_result: int = self._fibHelper(n - 1, fib_dict) + self._fibHelper(n - 2, fib_dict)
        fib_dict[n] =  fib_result
        return fib_result