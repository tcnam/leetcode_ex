from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit: int = 0
        buyInd: int = 0
        ind: int = 0
        while ind < len(prices):
            profit: int = prices[ind] - prices[buyInd]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                buyInd = ind
            ind+=1
        return maxProfit