package stack_and_queue;
import java.util.*;

class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character> sStack = new Stack<Character>();
        Stack<Character> tStack = new Stack<Character>();

        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == '#'){
                if (sStack.empty() == false){
                    sStack.pop();
                }
                else{
                    continue;
                }
            }
            else{
                sStack.push(s.charAt(i));
            }
        }

        for (int i = 0; i < t.length(); i++){
            if (t.charAt(i) == '#'){
                if (tStack.empty() == false){
                    tStack.pop();
                }
                else{
                    continue;
                }
            }
            else{
                tStack.push(t.charAt(i));
            }
        }

        while (tStack.isEmpty() == false && sStack.isEmpty() == false){
            if (tStack.pop() != sStack.pop()){
                return false;
            }
        }

        if (tStack.isEmpty() == false || sStack.isEmpty() == false){
            return false;
        }else{
            return true;
        }
    }
}
