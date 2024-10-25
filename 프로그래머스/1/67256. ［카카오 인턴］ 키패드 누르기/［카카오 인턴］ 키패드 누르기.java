class Solution {
    static String hand;
    static int currLeft = 10;
    static int currRight = 11;
    static int[] two = {3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 4};
    static int[] five = {2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 3};
    static int[] eight = {1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 2};
    static int[] zero = {0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 1};
    static String result = "";
    
    public String solution(int[] numbers, String hand) {
        this.hand = hand;
        // numbers = new int[]{5, 6, 2, 8, 1};
        // this.hand = "right";

        for (int i = 0; i < numbers.length; i++) {
            String currHand = selectHand(numbers[i]);
            result += currHand;
            
            if (currHand.equals("L")) {
                currLeft = numbers[i];
            }
            
            if (currHand.equals("R")) {
                currRight = numbers[i];
            }
            
            // System.out.println(currHand);
        }        
        
        return result;
    }
    
    public static String selectHand(int num) {
        if (num == 1 || num == 4 || num == 7) {
            return "L";
        } else if (num == 3 || num == 6 || num == 9) {
            return "R";
        } else if (num == 2) {
            int left = two[currLeft];
            int right = two[currRight];
            
            if (left == right) {
                return hand.equals("left") ? "L" : "R";
            } else {
                return left < right ? "L" : "R";
            }
        } else if (num == 5) {
            int left = five[currLeft];
            int right = five[currRight];
            
            if (left == right) {
                return hand.equals("left") ? "L" : "R";
            } else {
                return left < right ? "L" : "R";
            }
        } else if (num == 8) {
            int left = eight[currLeft];
            int right = eight[currRight];
            
            if (left == right) {
                return hand.equals("left") ? "L" : "R";
            } else {
                return left < right ? "L" : "R";
            }
        } else {
            int left = zero[currLeft];
            int right = zero[currRight];
            
            if (left == right) {
                return hand.equals("left") ? "L" : "R";
            } else {
                return left < right ? "L" : "R";
            }
        }
    }
    
}


 // 왼손만 갈 수 있는 1, 4, 7에서 2, 5, 8, 0을 갈 때 걸리는 거리를 저장
 // 오른손만 갈 수 있는 3, 6, 9에서 2, 5, 8, 0을 갈 때 걸리는 거리를 저장
 // 현재 위치에서 가야되는 곳이 2, 5, 8, 0이라면 얼마나 걸리는지 배열에서 가져옴
 // 같다면 주 사용 손을 선택