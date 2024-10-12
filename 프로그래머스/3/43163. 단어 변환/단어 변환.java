import java.util.*;

class Solution {        
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        Queue<String> queue = new LinkedList<>();
        Set<String> unvisitedSet = new HashSet<>(Arrays.asList(words));
        
        if (!unvisitedSet.contains(target)) {
            return answer;
        }
        
        queue.offer(begin);
        unvisitedSet.remove(begin);
        
        while (!queue.isEmpty()) {
            for (int i = 0; i < queue.size(); i++) {
                String curr = queue.poll();
                
                if (curr.equals(target)) {
                    return answer;
                }
                
                for (String word : unvisitedSet.toArray(new String[unvisitedSet.size()])) {
                    if (canConvert(curr, word)) {
                        queue.offer(word);
                        unvisitedSet.remove(word);
                    }
                }
            }
            
            answer++;
        }
        
        return 0; // 변환할 수 없는 경우
    }
    
    private boolean canConvert(String curr, String word) {
        int diffChar = 0;
        for (int i = 0; i < curr.length(); i++) {
            if (curr.charAt(i) != word.charAt(i)) {
                diffChar++;
            }
        }
        
        return diffChar == 1;
    }
    
}