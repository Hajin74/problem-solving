import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int n, int[][] computers) {
        boolean[] visited = new boolean[n];
        
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                bfs(computers, i, visited);
                count++;
            }
        }
        
        return count;
    }
    
    public void bfs(int[][] computers, int c, boolean[] visited) {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(c);
        
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            
            // 인접한 컴퓨터 탐색
            for (int i = 0; i < computers[curr].length; i++) {
                if (computers[curr][i] == 1) { // 1이면 연결된 컴퓨터
                    // 방문 안했다면 방문하고 큐에 넣기
                    if (!visited[i]) {
                        visited[i] = true;
                        queue.add(i);
                    }
                }
            }
        }
    }
}