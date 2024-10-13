import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] first = {1, 2, 3, 4, 5};
        int[] second = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] third =  {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] count = {0, 0, 0};
        
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == first[i % 5]) {
                count[0]++;
            }
            if (answers[i] == second[i % 8]) {
                count[1]++;
            }
            if (answers[i] == third[i % 10]) {
                count[2]++;
            }
        }
        
        ArrayList<Integer> answer = new ArrayList<>();
        
        int max = Math.max(count[2], Math.max(count[0], count[1]));
        for (int i = 0; i < 3; i++) {
            if (count[i] == max) {
                answer.add(i+1);
            }
        }
                
        return answer.stream()
            .mapToInt(x->x)
            .toArray();
    }
}