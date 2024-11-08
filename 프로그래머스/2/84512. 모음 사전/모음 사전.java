class Solution {
    static final char[] alpha =  {'A', 'E', 'I', 'O', 'U'};
    static final int[] count = {781, 156, 31, 6, 1};
    
    // 어떤 수가 4번째 자리에 올 때, 다음의 문자가 4번째 자리에 오려면 6번이 걸린다.
    // ___A_ : ___AA (1), ___AE (2), ___AI (3), ___AO (4), ___AU (5) , ___EA (6)
    // 어떤 수가 5번째 자리에 올 때, 다음의 문자가 5번째 자리에 오려면 1번이 걸린다.
    // ____E : ____I (1)
    
    // ex) AAAE
    // n자리 : n-1자리의 경우 + (alpha 인덱스  * alpha 인덱스의 count) + 1
    // 1자리 : 0 + (0 * 781) + 1 = 1
    // 2자리 : 1 + (0 * 156) + 1 = 2
    // 3자리 : 2 + (0 * 31) + 1 = 3
    // 4자리 : 3 + (1 * 6) + 1 = 10
    
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