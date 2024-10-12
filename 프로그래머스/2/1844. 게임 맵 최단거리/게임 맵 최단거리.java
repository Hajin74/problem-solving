import java.util.*;

class Solution {
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    public static int n;
    public static int m;
    public static int[][] maps;
    
    public int solution(int[][] maps) {
        this.n = maps.length;
        this.m = maps[0].length;
        this.maps = maps;
        
        bfs(0, 0);
        
        int answer = maps[n-1][m-1];
        
        if (answer == 1) {
            return -1;
        } else {
            return answer;
        }
    }
    
    public void bfs(int startX, int startY) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{startX, startY});
        
        // 큐가 빌 때까지
        while(!q.isEmpty()) {
            int[] pos = q.poll();
            int x = pos[0];
            int y = pos[1];
            
            // 인접한 노드들 방문
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                // 범위 제한
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                    continue;
                }
                
                if (maps[nx][ny] == 1) {
                    q.offer(new int[]{nx, ny});
                    maps[nx][ny] = maps[x][y] + 1;
                }
            }
        }
    }
}