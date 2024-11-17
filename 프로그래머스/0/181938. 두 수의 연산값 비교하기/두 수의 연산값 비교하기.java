class Solution {
    public int solution(int a, int b) {
        int str = Integer.parseInt(a + "" + b);
        int multiple = 2 * a * b;
        
        return str >= multiple ? str : multiple;
    }
}