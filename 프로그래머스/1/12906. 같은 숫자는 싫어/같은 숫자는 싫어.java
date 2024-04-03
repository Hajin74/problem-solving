import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> answerList = new ArrayList<>();
        
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < arr.length; i++) {
            if (stack.isEmpty() || stack.peek() != arr[i]) {
                 stack.push(arr[i]);
                 answerList.add(arr[i]);
            }
        }
        
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }
        
        
        return answer;
    }
}