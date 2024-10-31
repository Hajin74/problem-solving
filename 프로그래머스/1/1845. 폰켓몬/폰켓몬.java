import java.util.*;

class Solution {
    static int[] nums;
    static int answer;
    
    public int solution(int[] nums) {
        this.nums = nums;
        this.answer = 0;
        
//         comb(new ArrayList<Integer>(), 0);
        
//         //System.out.println("answer: "+ answer);
//         return answer;
        int max = nums.length / 2;
        
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        
        return max < set.size() ? max: set.size();
    }
    
    public static void comb(List<Integer> result, int depth) {
        if (depth == nums.length / 2) {  // n/2개 포켓못을 뽑음 
            Set<Integer> set = new HashSet<>(result);
            if (set.size() > answer) {
                answer = set.size();
            }
            
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            result.add(nums[i]);
            comb(result, depth + 1);
            result.remove(result.size() - 1); 
        }
    }
    
}