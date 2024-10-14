import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        Queue<Integer> leaves = new LinkedList<>();
        leaves.add(0);

        Queue<Integer> result = bfs(leaves, numbers);
        
        int answer = Collections.frequency(result, target);
        return answer;
    }
    
    public static Queue<Integer> bfs(Queue<Integer> leaves, int[] numbers) {
        for (int i = 0; i < numbers.length; i++) {
            Queue<Integer> temp = new LinkedList<>();
            while (!leaves.isEmpty()) {
                int leave = leaves.poll();
                temp.add(leave + numbers[i]);
                temp.add(leave - numbers[i]);
            }
            leaves = temp;
        }

        return leaves;
    }
}