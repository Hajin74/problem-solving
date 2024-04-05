import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
        Queue<Integer> bridge = new LinkedList<>();
        for(int i = 0; i < bridge_length; i++) {
            bridge.offer(0);
        }
        
        int index = 0;
        int current_weight = 0;
        while(index < truck_weights.length) {
            current_weight -= bridge.poll();
            answer++;
            
            if(current_weight + truck_weights[index] <= weight) {
                bridge.offer(truck_weights[index]);
                current_weight += truck_weights[index];
                index++;
            } else {
                bridge.offer(0);
            }
        }
        
        return answer + bridge_length;
    }
}