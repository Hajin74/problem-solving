import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        // scoville = new int[]{7};
        int answer = -1;
        
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (int s : scoville) {
            queue.add(s);
        }
        
        int count = 0;
        while (true) {
            if (queue.peek() >= K) {
                answer = count;
                break;
            }
            
            if (queue.size() == 1) {
                if (queue.peek() >= K) {
                    answer = count;
                }
                break;
            }
            
            int first = queue.poll();
            int second = queue.poll();
            int newScoville = first + second * 2;
            queue.add(newScoville);
            
            count++;
            //System.out.println(queue);
        }
        
        // if (answer == 0) {
        //     return -1;
        // }
        return answer;
    }
}