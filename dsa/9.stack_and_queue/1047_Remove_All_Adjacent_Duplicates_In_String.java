package stack_and_queue;
import java.util.*;

class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> sStack = new Stack<Character>();
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i ++){
            if (sStack.isEmpty() == false && sStack.peek() == s.charAt(i)){
                while (sStack.isEmpty() == false && sStack.peek() == s.charAt(i)){
                    sStack.pop();
                }
            }
            else{
                sStack.push(s.charAt(i));
            }
        }

        while (sStack.isEmpty() == false){
            result.append(sStack.pop());
        }

        return result.reverse().toString();
    }
}
