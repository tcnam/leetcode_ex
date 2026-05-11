from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit: int = 0
        buyInd: int = 0
        for i in range(0, len(prices), 1):
            tmpProfit: int = prices[i] - prices[buyInd]
            if tmpProfit == 0:
                continue
            if tmpProfit > 0:
                profit += tmpProfit
            buyInd = i
        return profit
            
            
        