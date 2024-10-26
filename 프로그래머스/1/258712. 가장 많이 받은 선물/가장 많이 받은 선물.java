import java.util.*;

class Solution {
    static int[] giftScore;
    static int[][] giftTable;
    static int[] nextGift;
    
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        
        this.giftScore = new int[friends.length];
        this.giftTable = new int[friends.length][friends.length];
        this.nextGift = new int[friends.length];
        
        fillOutGiftTable(friends, gifts);
        // printTable(friends);
        fillOutGiftScore(friends);
        printScore(giftScore, friends);
        
        for (int i = 0; i < friends.length; i++) {
            for (int j = i+1; j < friends.length; j++) {
                // System.out.println("i:" + i + ", j: " + j);
                if (i != j) {
                    // 교류한 적 없거나 같으면 선물 지수 비교
                    if (giftTable[i][j] == giftTable[j][i] || (giftTable[i][j] == 0 && giftTable[j][i] == 0)) {
                        if (giftScore[i] > giftScore[j]) {
                            nextGift[i]++;
                        } else if (giftScore[i] < giftScore[j]) {
                            nextGift[j]++;
                        } 
                    } else {
                        if (giftTable[i][j] > giftTable[j][i]) {
                            nextGift[i]++;
                        } else if (giftTable[i][j] < giftTable[j][i]) {
                            nextGift[j]++;
                        } 
                    }
                }
                // printScore(nextGift, friends);
            }
        }
        
        answer = Arrays.stream(nextGift).max().getAsInt();
        
        // printScore(nextGift, friends);
        
        return answer;
    }
    
    public static void fillOutGiftScore(String[] friends) {
        for (int i = 0; i < friends.length; i++) {
            int giveScore = Arrays.stream(giftTable[i]).sum();
            int takeScore = 0;
            
            for (int j = 0; j < friends.length; j++) {
                takeScore += giftTable[j][i];
            }
            giftScore[i] = giveScore - takeScore;
        }
    }
    
    public static void fillOutGiftTable(String[] friends, String[] gifts) {
        for (int i = 0; i < gifts.length; i++) {
            String[] data = gifts[i].split(" ");
            String giver = data[0]; // 주는 사람
            String taker = data[1]; // 받는 사람
            
            for (int j = 0; j < friends.length; j++) {
                if (giver.equals(friends[j])) {
                    for (int k = 0; k < friends.length; k++) {
                        if (taker.equals(friends[k])) {
                            giftTable[j][k]++;
                            break;
                        }
                    }
                    break;
                }
            }
        }
    }
                    
    public static void printTable(String[] friends) {
        for (int i = 0; i < friends.length; i++) {
            for (int j = 0; j < friends.length; j++) {
                System.out.print(giftTable[i][j] + " ");
            }
            System.out.println();
        }
    }
    
    public static void printScore(int[] score, String[] friends) {
        for (int i = 0; i < friends.length; i++) {
            System.out.print(score[i] + " ");
        }
        System.out.println();
    }
}