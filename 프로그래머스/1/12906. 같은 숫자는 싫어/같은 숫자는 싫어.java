import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        
        int i = 0;
        while (i < arr.length - 1) {
            int now = arr[i];
            int next = arr[i+1];
            
            if (now != next) {
                arrayList.add(now);
            }
            
            i++;
        }
        
        arrayList.add(arr[arr.length - 1]);
                
        return arrayList.stream()
            .mapToInt(x->x)
            .toArray();
    }
}