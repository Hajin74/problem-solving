class Solution {
    static int[] memo;
    
    public int solution(int n) {
        memo = new int[100001];
        memo[0] = 0;
        memo[1] = 1;
        return fibo(n) % 1234567;
    }
    
    public static int fibo(int n) {
        if (n == 0 || n == 1 || memo[n] > 0) {
            return memo[n];
        } else {
            memo[n] = fibo(n-1) % 1234567 + fibo(n-2) % 1234567;
        }
        
        return memo[n];
    }
}