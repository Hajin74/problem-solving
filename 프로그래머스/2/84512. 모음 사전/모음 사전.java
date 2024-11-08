class Solution {
    static final char[] alpha =  {'A', 'E', 'I', 'O', 'U'};
    static final int[] count = {781, 156, 31, 6, 1};
    
    // 어떤 수가 1자리에 올 때 그 뒤에 781번부터 시작이다.
    // A_____ : 1 ~ 781, E_____ : 782 ~ 1562 
    // 어떤 수가 2자리에 올 때 그 뒤에 156번부터 시작이다.
    // _A___ : 3905 ~ 4060, _E___ : 4061 ~ 4215
    
    public int solution(String word) {
        int sum = 0;
        for (int i = 0; i < word.length(); i++) {
            System.out.println(word.charAt(i));
            
            if (word.charAt(i) == 'A') {
                sum += count[i] * 0;
            } else if (word.charAt(i)== 'E') {
                sum += count[i] * 1;
            } else if (word.charAt(i) == 'I') {
                sum += count[i] * 2;
            } else if (word.charAt(i) == 'O') {
                sum += count[i] * 3;
            } else if (word.charAt(i) == 'U') {
                sum += count[i] * 4;
            }
            
            sum += 1;
            System.out.println(sum);
        }
        
         System.out.println(sum);
        return sum;
    }
}