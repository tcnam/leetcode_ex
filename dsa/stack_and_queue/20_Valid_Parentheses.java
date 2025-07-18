package stack_and_queue;
import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        Map<Character, Character> bracketMap = new HashMap<Character, Character>();
        bracketMap.put(')', '(');
        bracketMap.put(']', '[');
        bracketMap.put('}', '{');

        for (int i=0; i < s.length(); i++){
            if (stack.empty() == true 
                || bracketMap.containsKey(s.charAt(i)) == false 
                || stack.peek() != bracketMap.get(s.charAt(i))) {
                stack.push(s.charAt(i));
            }
            else {
                stack.pop();
            }
        }
        if (stack.empty() == true){
            return true;
        }
        return false;
    }
}