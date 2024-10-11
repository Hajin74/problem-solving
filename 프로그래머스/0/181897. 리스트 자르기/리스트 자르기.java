import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int a = slicer[0];
        int b = slicer[1];
        int c = slicer[2];
        
        if (n == 1) {
            return Arrays.copyOfRange(num_list, 0, b+1);
        } else if (n == 2) {
            return Arrays.copyOfRange(num_list, a, num_list.length);
        } else if (n == 3) {
            return Arrays.copyOfRange(num_list, a, b+1);
        } else {
            List<Integer> list = new ArrayList<>();
            for (int i = a; i <= b; i += c) {
                list.add(num_list[i]);
            }
            
            int[] arr = list.stream()
                .mapToInt(Integer::intValue)
                .toArray();
            
            return arr;
        }
        
    }
}