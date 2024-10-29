import java.util.*;

class Solution {
    static int[][] dungeons;
    static int k;
    static boolean[] visited;
    static int answer = 0;
    
    public int solution(int k, int[][] dungeons) {
        // dungeons = new int[][]{{78, 18}, {70, 11}, {67, 9}, {60, 8}, {59, 2}, {57, 54}};
        // k = 78;
        
        
        this.dungeons = dungeons;
        this.k = k;
        this.visited = new boolean[dungeons.length];
        
        dfs(new ArrayList<>());
        // System.out.println(answer);
        
        return answer;
    }
    
    public static void dfs(List<int[]> current) {
        if (current.size() == dungeons.length) { // 모든 던전 다 방문했으면 던전 탐색 중지
            setMaxAnswer(current.size());
            // printList(current);
            return;
        }
        
        for (int i = 0; i < dungeons.length; i++) {
            if (!visited[i]) {
                if (k < dungeons[i][0]) { // 최소 필요 피로도가 모자르다면 던전 탐색 중지
                    setMaxAnswer(current.size());
                    // printList(current);
                    continue;
                }
                
                visited[i] = true;
                current.add(dungeons[i]);
                k -= dungeons[i][1]; // 해당 던전 소모 피로도만큼 깎임
                
                dfs(current);
                
                // 백트래킹 (상태복원)
                visited[i] = false;
                current.remove(current.size() - 1);
                k += dungeons[i][1]; // 해당 던전 소모 피로도만큼 회복
            }
        }
    }
    
    public static void setMaxAnswer(int now) {
        if (now > answer) {
            answer = now;
        }
    }
    
    public static void printList(List<int[]> current) {
        for (int i = 0; i < current.size(); i++) {
            for (int j = 0; j < 2; j++) {
                System.out.print(current.get(i)[j] + " ");
            }
            System.out.println();
        }
        System.out.println("k: " + k + ", result: " + current.size());
    }
}

// 던전의 모든 순서를 다 탐색하면서 탐험할 수 있는 던전의 최대 개수를 구한다.
// 모든 순서를 탐색하는 걸 어떻게 구현하지?
// 아이디어 1: dfs + 백트래킹
// 현재 노드 방문 처리, 인접한 노드 방문, 방문 안했다면 dfs 돌리기