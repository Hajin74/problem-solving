import java.util.*;

class Solution {
    public static int n;
    public static int m;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    
    public int solution(int[][] maps) {
        this.n = maps.length;
        this.m = maps[0].length;
    
        bfs(maps, 0, 0);
    
        if (maps[n-1][m-1] == 1) {
            return -1;
        } else {
            return maps[n-1][m-1];
        }
    }

    public static void bfs(int[][] maps, int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        
        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            
            for (int i = 0; i < 4; i++) {
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];
                
                // 범위 제한
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                    continue;
                }
                
                if (maps[nx][ny] == 1) {
                    maps[nx][ny] = maps[now[0]][now[1]] + 1; // 최단경로로 방문처리
                    queue.add(new int[]{nx, ny});
                }
            }
        }
    }
}