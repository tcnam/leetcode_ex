package stack_and_queue;
import java.util.*;

class Solution {
    public String makeGood(String s) {
        Stack<Character> charStack = new Stack<Character>();
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++){
            if (charStack.isEmpty() == false 
                && Character.toUpperCase(s.charAt(i)) == Character.toUpperCase(charStack.peek())
                && (int) s.charAt(i) != (int) charStack.peek())   {
                    charStack.pop();
                }
            else{
                charStack.push(s.charAt(i));
            }
        }

        while (charStack.isEmpty()== false){
            result.append(charStack.pop());
        }
        return result.reverse().toString();
    }
}
