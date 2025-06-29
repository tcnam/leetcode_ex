package hash_table;
import java.util.*;

class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        Map<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        int maxFreq = 0;
        for (int i = lowLimit; i <= highLimit; i++){
            int sumDigits = this.sumOfDigits(i);
            if (hashMap.containsKey(sumDigits)){
                hashMap.replace(sumDigits, hashMap.get(sumDigits) + 1);
            }
            else{
                hashMap.put(sumDigits, 1);
            }

            if (maxFreq < hashMap.get(sumDigits)){
                maxFreq = hashMap.get(sumDigits);
            }
        }
        return maxFreq;
    }

    private int sumOfDigits(int num){
        int result = 0;
        while (num > 0){
            result += num % 10;
            num = num/10;
        }
        return result;
    }
}
