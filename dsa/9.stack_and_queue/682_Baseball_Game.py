import typing as t

class Solution:
    def calPoints(self, operations: t.List[str]) -> int:
        stack: t.List[int] = []
        for op in operations:
            if op == "+":
                num2: int = stack[-1]
                num1: int = stack[-2]
                num: int = num1 + num2
                stack.append(num)
            elif op == "C":
                stack.pop()
            elif op == "D":
                num: int = stack[-1] * 2
                stack.append(num)
            else:
                stack.append(int(op))
        
        result: int = 0
        for num in stack:
            result += num
        
        return result
