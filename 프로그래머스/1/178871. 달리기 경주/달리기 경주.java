import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {   
        
        // 맵 형태로 저장 (선수이름 : 순위)
        HashMap<String, Integer> playerMap = new HashMap<>();
        for (int i = 0; i < players.length; i++) {
            playerMap.put(players[i], i);
        }
        
        for (int i = 0; i < callings.length; i++) {
            String playerName = callings[i];
            int playerRank = playerMap.get(playerName);
            
            // 앞 사람과 자리 교환
            String temp = players[playerRank - 1]; 
            players[playerRank - 1] = playerName; 
            players[playerRank] = temp;
            
            // 순위 업데이트
            playerMap.put(players[playerRank], playerRank);
            playerMap.put(players[playerRank - 1], playerRank - 1);
           
            // System.out.println(playerRank);
        }
        
        return players;
    }
}

// 이름이 불릴 때 앞 인덱스의 플레이어와 자리를 바꾸게 됨
// List, indexOf로 풀이 -> 시간 초과 -> o(1)로 찾을 수 있는 map으로 변환 
