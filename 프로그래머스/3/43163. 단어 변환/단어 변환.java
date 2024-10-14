import java.util.*;

class Solution {
    static boolean[] visited;
    
    public int solution(String begin, String target, String[] words) {
        int answer = 0;

        Queue<String> queue = new LinkedList<>();
        Set<String> set = new HashSet<>(Arrays.asList(words));

        if (!set.contains(target)) { // 변환할 수 있는 단어 목록에 타켓이 없음
            return 0;
        }

        queue.offer(begin);
        set.remove(begin);

        while (!queue.isEmpty()) {
            for (int i = 0; i < queue.size(); i++) {
                String now = queue.poll();

                if (now.equals(target)) {
                    return answer;
                }

                // 아직 쓰지 않은 단어들 : set
                for (String word : set.toArray(new String[set.size()])) {
                    // 변환 가능하면 큐에 단어 추가하고, set에서 제거 (set으로 방문처리)
                    if (canConvert(now, word)) {
                        queue.offer(word);
                        set.remove(word); 
                    }
                }
            }

            answer++;
        }

        return 0;
    }
    
    public static boolean canConvert(String a, String b) {
        int count = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                count++;
            }
        }
        
        return count == 1;
    }
}