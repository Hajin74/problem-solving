import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        // bfs 돌면서 연산 결과를 저장하고, 그 중에서 target 수에 만족하는 개수를 반환 
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        
        for (int i = 0; i < numbers.length; i++) {
            int num = numbers[i];
            
            ArrayList<Integer> list = new ArrayList<>();
            while (!queue.isEmpty()) {
                int now = queue.poll();
                list.add(now + num);
                list.add(now - num);
            }
            
            for (Integer value : list) {
                queue.offer(value); 
            }
        } 
    
        answer = Collections.frequency(queue, target);
        return answer;
    }
}