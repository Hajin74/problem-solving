import java.util.*;

// 1부터 n까지 학생이 있겠지
// lost는 범위(1~n)중에 각 옆에 번호 학생에게 체육복을 빌릴 수 있음
// 각 옆 학생이 reserve에 있으면 얘는 빌린 거로 처리하여서
// 체육복 주인은 reserve에서 삭제

class Solution {
    
     public static void main(String[] args) {
        Solution solution = new Solution();
        
        int n = 5; // 학생 수
        int[] lost = {2, 3}; // 체육복을 잃어버린 학생
        int[] reserve = {3, 4}; // 여분의 체육복이 있는 학생

        // solution 메서드 호출
        int result = solution.solution(n, lost, reserve);
        
        // 결과 출력
        System.out.println("체육복을 가진 학생 수: " + result); // 결과 출력
    }
    
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length; // 체육복 있는 학생
        
        List<Integer> reserveList = new ArrayList<>();
        for (int value : reserve) {
            reserveList.add(value);
        }
        Collections.sort(reserveList);
        
        List<Integer> lostList = new ArrayList<>();
        for (int value : lost) {
            lostList.add(value);
        }
        Collections.sort(lostList);

        // 여벌 학생들 중 도난 당한 학생은 여벌 리스트에서 제외하기
        ArrayList<Integer> temp = new ArrayList<>();
        for (Integer student : lostList) {
            if (reserveList.contains(student)) {
                temp.add(student);
            }
        }

        for (Integer student: temp) {
            if (reserveList.contains(student)) {
                reserveList.remove(Integer.valueOf(student));
                lostList.remove(Integer.valueOf(student));
                answer++;
            }
        }
        
        // 빌려줄 사람이 없을 때도 대처
        for (Integer student : lostList) {
            int[] dx = {-1, 1};
            
            for (int i = 0; i < 2; i++) {
                int nx = student + dx[i];
                
                if (reserveList.contains(nx)) {
                    reserveList.remove(Integer.valueOf(nx));
                    answer++;
                    break;
                }
            }
        }
        
        return answer;
    }
}