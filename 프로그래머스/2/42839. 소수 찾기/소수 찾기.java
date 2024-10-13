import java.util.*;

class Solution {
    static HashSet<Integer> set = new HashSet<>();
    static boolean[] visited;
    
    public int solution(String numbers) {
        this.visited = new boolean[numbers.length()];
        int answer = 0;
        
        dfs("", 0, numbers);
        
        return set.size();
    }
    
    private static void dfs(String comb, int depth, String numbers) {
        if (!comb.isEmpty()) {
            int num = Integer.parseInt(comb);
            if (isPrime(num)) {
                set.add(num);
            }
        }
        
        if (depth == numbers.length()) {
            return;
        }
        
        for (int i = 0; i < numbers.length(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(comb + numbers.charAt(i), depth+1, numbers);
                visited[i] = false;
            }
        }
    }
    
    private static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        
        return true;
    }
}