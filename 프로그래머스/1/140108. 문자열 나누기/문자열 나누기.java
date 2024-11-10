class Solution {
    public int solution(String s) {
        int answer = 0;
        
        int firstCount = 0, restCount = 0;
        char first = '*';
        for (int i = 0; i < s.length(); i++) {
            if (firstCount == 0) {
                first = s.charAt(i);
                firstCount++;
                continue;
            }
            
            if (s.charAt(i) == first) {
                firstCount++;
            } else {
                restCount++;
            }
            
            if (firstCount == restCount) {
                System.out.println(first + ", " + firstCount + ", " + restCount);
                answer++;
                firstCount = 0;
                restCount = 0;
            }
        
        }
        
        if (firstCount > 0) {
            answer++;
        }
        
        return answer;
    }
}