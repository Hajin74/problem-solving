import java.util.*;

class Solution {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int n;
    static int m;
    
    public int solution(String[] maps) {
        // maps = new String[]{"SELXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"};
            
        int answer = -1;
        
        this.n = maps.length;
        this.m = maps[0].length();
        
        // 1. 시작점부터 레버까지 최단거리 찾기
        
        // 방문처리 맵 초기화
        int[][] visited = new int[n][m];
        Arrays.stream(visited).forEach(n -> Arrays.fill(n, -1));
        
        // 시작 좌표 찾기
        int[] startIndex = {0, 0};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (maps[i].charAt(j) == 'S') {
                    startIndex = new int[]{i, j};
                    break;
                }
            }
        }
        
        int[] leverIndex = bfs(maps, visited, startIndex, 'L');
        int distance1 = visited[leverIndex[0]][leverIndex[1]];
        // printMap(visited);
                
        if (distance1 == 0) {
            return answer;
        }
        
        
        // 2. 레버부터 출구까지 최단거리 찾기
        
        // 방문처리 맵 초기화
        visited = new int[n][m];
        Arrays.stream(visited).forEach(n -> Arrays.fill(n, -1));
        
        int[] exitIndex = bfs(maps, visited, leverIndex, 'E');
        int distance2 = visited[exitIndex[0]][exitIndex[1]];
        // printMap(visited);
        
        if (distance2 == 0) {
            return answer;
        }

        answer = distance1 + distance2;
        
        return answer;
    }
    
    public static int[] bfs(String[] maps, int[][] visited, int[] startIndex, char target) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(startIndex);
        
        int startX = startIndex[0];
        int startY = startIndex[1];
        visited[startX][startY] = 0;
        
        int[] targetIndex = {startX, startY};
        
        while (!queue.isEmpty()) {
            int[] currLoc = queue.poll();
            int currX = currLoc[0];
            int currY = currLoc[1];
            // System.out.println(currX + ", " + currY);
            
            for (int i = 0; i < 4; i++) {
                int nextX = currX + dx[i];
                int nextY = currY + dy[i];
                
                // 범위 제한
                if (nextX < 0 || nextY < 0 || nextX >= n || nextY >= m) {
                    continue;
                }
                
                 // 다음 칸이 도착지(target)일 경우
                if (maps[nextX].charAt(nextY) == target && visited[nextX][nextY] == -1) {
                    visited[nextX][nextY] = visited[currX][currY] + 1; // 거리 +1
                    targetIndex = new int[]{nextX, nextY};
                    break;
                }
                
                // 다음 칸이 통로이고, 아직 방문하지 않은 경우
                if (maps[nextX].charAt(nextY) != 'X' && visited[nextX][nextY] == -1) {
                    queue.offer(new int[]{nextX, nextY});
                    visited[nextX][nextY] = visited[currX][currY] + 1; // 거리 +1
                }
            }
            
            // 목적치에 도착했으면 탐색 중지
            if (targetIndex[0] != startX) {
                break;
            }
        }
        
        return targetIndex;
    }
    
    public static void printMap(int[][] map) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(map[i][j] + " ");
            }
            System.out.println();
        }
    }
}

// 인접한 모든 칸을 탐색한다.
// 레버를 만나면 문을 연다.
// 문을 열면 출구로 탈출 할 수 있다.
// 레버를 안당기고 도착한 출구는 의미가 없다.
// 반드시 레버를 열고, 출구로 탈출하는 순서여야 한다.

// 방법1: dfs + 백트래킹
// 방법2: 레버까지 bfs * 출구까지 bfs -> 선택