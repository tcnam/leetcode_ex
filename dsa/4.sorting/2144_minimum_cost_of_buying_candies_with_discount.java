package sorting;

class Solution {
    public int minimumCost(int[] cost) {
        int[] countCost = new int[101];
        int result = 0;
        for (int i = 0; i < cost.length; i++){
            countCost[cost[i]] += 1;
        }
        int count = 3;
        for (int i = 100; i > 0; i--){
            while (countCost[i] > 0){
                if (count == 1) {
                    count = 3;
                }
                else {
                    count -= 1;
                    result += i; 
                }
                countCost[i] -= 1;
            }
        }
        return result;
    }
}
