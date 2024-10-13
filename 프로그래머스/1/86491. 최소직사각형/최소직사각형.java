import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        ArrayList<Integer> longSide = new ArrayList<>();
        ArrayList<Integer> shortSide = new ArrayList<>();
        
        for (int i = 0; i < sizes.length; i++) {
            if (sizes[i][0] > sizes[i][1]) {
                longSide.add(sizes[i][0]);
                shortSide.add(sizes[i][1]);
            } else {
                longSide.add(sizes[i][1]);
                shortSide.add(sizes[i][0]);
            }
        }

        return Collections.max(longSide) * Collections.max(shortSide);
    }
}