import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] query) {
        int[] answer = Arrays.copyOf(arr, arr.length);
        
        for (int i = 0; i < query.length; i++) {
            int index = query[i];
            
            if (i % 2 == 0) { // 짝수 : 뒷부분 자르기
                answer = Arrays.copyOfRange(answer, 0, index+1);
            } else { // 홀수 : 앞부분 자르기
                answer = Arrays.copyOfRange(answer, index, answer.length);
            }
        }
        
        return answer;
    }
}