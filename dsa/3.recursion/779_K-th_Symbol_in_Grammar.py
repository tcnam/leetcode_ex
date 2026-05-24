class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        row: str = self.constructRow(n)
        print(row)
        return int(row[k - 1])
        # return bin(k - 1).count("1") % 2

    def constructRow(self, n: int) -> str:
        if n == 1:
            return "0"
        
        row: str = self.constructNextRow(
            self.constructRow(n - 1)
        )

        return row

    
    def constructNextRow(self, s:str) -> str:
        next_row: str = ""
        for char in s:
            if char == "0":
                next_row += "01"
            else:
                next_row += "10"
        return next_row