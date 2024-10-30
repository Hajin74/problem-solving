import java.util.*;

class Solution {
    static int[][] users;
    static int[] emoticons;
    
    static int[] rate = {10, 20, 30, 40};
    static int[] rateComb;
    static int maxMember, maxProfit;
    
    public int[] solution(int[][] users, int[] emoticons) {
        this.users = users;
        this.emoticons = emoticons;
        this.rateComb = new int[emoticons.length];
        
        comb(0);
        
        return new int[]{maxMember, maxProfit};
    }
    
    public static void comb(int depth) {
        if (depth == rateComb.length) { // 이모티콘 개수만큼, 할인률 개수 뽑음 (중복 조합)
            cal();
            // printArr(rateComb);
            return;
        }
        
        for (int i = 0; i < 4; i++) {
            rateComb[depth] = rate[i];
            comb(depth + 1);
        }
    }
    
    public static void cal() {
        int member = 0;
        int profit = 0;
        
        for (int[] user : users) {
            int discount = user[0]; // 사용자가 무조건 구입하는 할인률
            int price = user[1]; // 사용자가 플러스에 가입하는 금액
            
            int sum = 0; // 이모티콘 총 구매 금액
            for (int i = 0; i < rateComb.length; i++) {
                if (rateComb[i] >= discount) { // 사용자가 무조건 구입하는 할인률 이상이면
                    sum += (emoticons[i] / 100) * (100 - rateComb[i]); // 할인된 금액으로 계산
                }
            }
            
            if (sum >= price) { // 플러스에 가입하는 금액보다 많이 샀으면
                member++; // 플러스 가입
            } else {
                profit += sum; // 수익으로 계산
            }
        }
        
        if (member > maxMember) {
            maxMember = member;
            maxProfit = profit;
            return;
        } else if (member == maxMember) { // 같은 가입자여도
            if (profit > maxProfit) { // 수익이 더 높은걸 선택
                maxProfit = profit;
            }
        }
    }
    
    public static void printArr(int[] arr) {
        for (int a: arr) {
            System.out.print(a + " ");
        }
        System.out.println();
    }
    
}