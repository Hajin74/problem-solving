import java.util.List;
import java.util.Arrays;
import java.util.stream.IntStream;

class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        int[] firstArr = Arrays.copyOfRange(arr, intervals[0][0], intervals[0][1] + 1);
        int[] secondArr = Arrays.copyOfRange(arr, intervals[1][0], intervals[1][1] + 1);
        
        int[] answer = IntStream.concat(Arrays.stream(firstArr), Arrays.stream(secondArr)).toArray();
        return answer;
    }
}