import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> list = new ArrayList<>();
        
        for (Integer e : arr) {
            for (int i = 0; i < e; i++) {
                list.add(e);
            }
        }
        
        int[] answer = list.stream()
                            .mapToInt(Integer::intValue)
                            .toArray();
        
        return answer;
    }
}