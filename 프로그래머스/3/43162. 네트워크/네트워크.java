import java.util.*;

class Solution {
    static boolean[] visited;
    
    public int solution(int n, int[][] computers) {
        this.visited = new boolean[n];
        
        int network = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                bfs(n, computers, i);
                network++;
            }
        }
        
        return network;
    }
    
    public static void bfs(int n, int[][] computers, int v) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(v);
        visited[v] = true; // 현재 컴퓨터 방문처리
        
        while (!queue.isEmpty()) {
            int now = queue.poll();
            
            for (int i = 0; i < n; i++) {
                int next = computers[now][i];
                
                // 방문하지 않고, 연결이 되어 있는 컴퓨터면
                if (!visited[i] && next == 1 ) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }
}