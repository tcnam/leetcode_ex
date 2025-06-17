class Solution {
    public int maxProfit(int[] prices) {
        int buyInd = 0;
        int maxProfit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] >= prices[buyInd]) {
                int tempProfit = prices[i] - prices[buyInd];
                if (tempProfit > maxProfit) {
                    maxProfit = tempProfit;
                }
            }
            else {
                buyInd = i;
            }
        }
        return maxProfit;
    }
}