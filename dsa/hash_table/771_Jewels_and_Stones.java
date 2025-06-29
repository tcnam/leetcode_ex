package hash_table;
import java.util.*;

class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> hashSet = new HashSet<Character>();
        int result = 0;

        for (int i = 0; i < jewels.length(); i++){
            if (hashSet.contains(jewels.charAt(i)) == false){
                hashSet.add(jewels.charAt(i));
            }
        }

        for (int j = 0; j < stones.length(); j++){
            if (hashSet.contains(stones.charAt(j)) == true){
                result += 1;
            }
        }
        return result;
    }
}
