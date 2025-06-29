package hash_table;
import java.util.*;

class Solution {
    public int partitionString(String s) {
        Set<Character> hashSet = new HashSet<Character>();
        int result = 0;
        for (int i = 0; i < s.length(); i++){
            if (hashSet.contains(s.charAt(i)) == true){
                result += 1;
                hashSet.clear();
            }
            hashSet.add(s.charAt(i));
        }
        return result + 1;
    }
}