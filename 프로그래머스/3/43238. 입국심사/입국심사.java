import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        // times = new int[]{2};
        // n = 4;
        Arrays.sort(times);
        
        long answer = 0;
        long left = times[0];
        long right = (long)times[times.length - 1] * n;
        
        while (left <= right) {
            long mid = (left + right) / 2;
            System.out.println("mid: " + mid);
            
            long count = 0;
            for (int time : times) {
                count += mid / time;
            }
            // System.out.println("count: " + count);
            
            if (count < n) { // 시간 안에 심사를 볼 수 없으면
                left = mid + 1;
            } else { // 시간안에 심사를 볼 수 있거나 남으면
                answer = mid;
                right = mid - 1;
            }
        }
        
        // System.out.println("answer: " + answer);
        return answer;
    }
}


// 모든 사람이 심사를 받는 걸리는 시간을 찾아야 하므로, 이것을 탐색의 범위로 두자.
// 가장 적게 걸리는 시간은 0, 가장 오래 걸리는 시간은 가장 긴 심사 시간 * 사람 수이다.
// 이분탐색을 진행하면서 mid의 시간동안 몇 명이나 심사가 가능한지 세어본다.