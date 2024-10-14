import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        List<Integer> yellowXList = new ArrayList<>();
        List<Integer> yellowYList = new ArrayList<>();
        
        for (int i = yellow; i >= Math.sqrt(yellow); i--) {
            if (yellow % i == 0) {
                yellowXList.add(i);
                yellowYList.add(yellow / i);
            }
        }        
        
        for (int i = 0; i < yellowXList.size(); i++) {
            int yellowX = yellowXList.get(i);
            int yellowY = yellowYList.get(i);
            
            if (2 * (yellowX + yellowY + 2) == brown) {
                return new int[]{yellowX + 2, yellowY + 2};
            }
        }
        
        return new int[]{0, 0};
    }
}