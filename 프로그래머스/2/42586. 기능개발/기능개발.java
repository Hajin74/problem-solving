import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        
        // 작업 일수 계산
        for (int i = 0; i < progresses.length; i++) {
            // 나머지가 있으면 올림
            int day = (int)(Math.ceil((100.0 - progresses[i]) / speeds[i]));
            queue.add(day);
        }
        
        while (!queue.isEmpty()) {
            int days = queue.poll();
            int count = 1;
            
            while(!queue.isEmpty() && queue.peek() <= days) {
                queue.poll();
                count++;
            }
            
            answer.add(count);
        }
        
        return answer;
    }
}