import java.util.Stack;

class Solution {
    boolean solution(String s) {
        boolean answer = true;

        Stack<String> stack = new Stack<>();

        try {
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                if (c == '(') {
                    stack.push(String.valueOf(c));
                } else {
                    stack.pop();
                }
            }
        } catch (Exception e) {
            answer = false;
        }

        if (!stack.isEmpty()) {
            answer = false;
        }

        return answer;
    }
}