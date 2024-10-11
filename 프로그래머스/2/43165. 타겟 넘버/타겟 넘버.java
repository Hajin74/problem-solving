import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(int[] numbers, int target) {
        List<Integer> leaves = new ArrayList<>();
        leaves.add(0);
        
        for (Integer num : numbers) {
            List<Integer> temp = new ArrayList<>();
            for (Integer leaf : leaves) {
                temp.add(leaf + num);
                temp.add(leaf - num);
            }
            leaves = temp;
        }
        
        int answer = 0;
        for (Integer leaf : leaves) {
            if (leaf == target) {
                answer++;
            }
        }
        
        return answer;
    }
}