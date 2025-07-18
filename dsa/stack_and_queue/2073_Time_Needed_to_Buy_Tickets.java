package stack_and_queue;

class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int result = 0;
        for (int i = 0; i < tickets.length; i++){
            if (i < k){
                if (tickets[i] >= tickets[k]){
                    result += tickets[k];
                }
                else{
                    result += tickets[i];
                }
            }
            else if (i > k){
                if (tickets[i] >= tickets[k] - 1){
                    result += tickets[k] - 1;
                }
                else{
                    result += tickets[i];
                }
            }
            else{
                result += tickets[i];
            }
        }
        return result;
    }
}
