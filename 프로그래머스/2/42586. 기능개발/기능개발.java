import java.util.ArrayList; 
import java.util.Stack;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) { 
        ArrayList<Integer> result = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < progresses.length; i++) {
            int days =  (100 - progresses[i]) / speeds[i];
            int remain =  (100 - progresses[i]) % speeds[i];
            if (remain > 0) {days++;}

            if (i > 0) {
                if (stack.get(0) < days) {
                    result.add(stack.size());
                    stack.clear();
                }
            }
            stack.push(days);
        }
        result.add(stack.size());

        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        
        return answer;
    }
}