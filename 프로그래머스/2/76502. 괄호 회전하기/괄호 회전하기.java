import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        // s = "([{)}]";
        
        for (int i = 0; i < s.length(); i++) {
            String newStr = s.substring(1) + s.charAt(0);
            if (isCorrectBrackets(newStr)) {
                answer++;
            }
            
            s = newStr;
        }
        
        return answer;
    }
    
    public static boolean isCorrectBrackets(String s) {
        boolean answer = true;
        
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.size() == 0) {
                    return false;
                }
                
                char p = stack.pop();
                if (c == ')') {
                    if (p != '(') {
                        return false;
                    }
                } else if (c == ']') {
                    if (p != '[') {
                        return false;
                    }
                } else if (c == '}') {
                    if (p != '{') {
                        return false;
                    }
                }
            }
        }
        
        if (stack.size() != 0) {
            answer = false;
        }
        
        return answer;
    }
    
}