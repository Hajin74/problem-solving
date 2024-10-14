import java.util.*;

class Solution {
    public static void main(String[] args) {
        Solution solution = new Solution();
    }
    
    public List<Integer> solution(int[] array, int[][] commands) {
        List<Integer> arrayList = new ArrayList<>();
        for (Integer num : array) {
            arrayList.add(num);
        }
        
        List<Integer> answerList = new ArrayList<>();
        
        for (int i = 0; i < commands.length; i++) {
            int start = commands[i][0] - 1;
            int end = commands[i][1];
            int k = commands[i][2] - 1;
            
            List<Integer> copiedSubList = new ArrayList<>(arrayList.subList(start, end));
            Collections.sort(copiedSubList);
            answerList.add(copiedSubList.get(k));
        }
        
        return answerList;
    }
}