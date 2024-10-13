import java.util.*;

class Solution {
    List<String> pathList = new ArrayList<>();
    boolean[] visited;
    
    public String[] solution(String[][] tickets) {
        this.visited = new boolean[tickets.length];
        
        dfs(tickets, "ICN", 0, "ICN");
        
        Collections.sort(pathList);
        
        return pathList.get(0).split(" ");
    }
    
    private void dfs(String[][] tickets, String current, int count, String path) {
        if (count == tickets.length) {
            pathList.add(path);
            return;
        }
        
        for (int i = 0; i < tickets.length; i++) {
            // 아직 사용하지 않은 티켓 중에서, 현재 위치에서 갈 수 있는 티켓 찾기
            if (!visited[i] && current.equals(tickets[i][0])) {
                visited[i] = true;
                dfs(tickets, tickets[i][1], count + 1, path + " " + tickets[i][1]);
                visited[i] = false;
            }
        }
    
    }
}