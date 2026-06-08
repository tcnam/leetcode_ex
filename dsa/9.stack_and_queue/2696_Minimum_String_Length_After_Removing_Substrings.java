package stack_and_queue;
import java.util.*;

class Solution {
    public int minLength(String s) {
        Map<Character, Character> map = new HashMap<Character, Character>();
        map.put('D', 'C');
        map.put('B', 'A');
        Stack<Character> charStack = new Stack<Character>();
        int len = s.length();

        for(int i = 0; i < s.length(); i++){
            if (charStack.isEmpty() == false 
                && map.containsKey(s.charAt(i)) == true
                && map.get(s.charAt(i)) == charStack.peek()){
                    charStack.pop();
                    len -= 2;
            }
            else{
                charStack.push(s.charAt(i));
            }
        }
        return len;
    }
}
