class Solution {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] citations = {0, 0, 0};
        int result = solution.solution(citations);
        System.out.println("result : " + result);
    }
    
    public int solution(int[] citations) {
        int hIndex = 0;

        for (int h = 0; h <= citations.length; h++) {
            int count = 0;
            for (Integer citation : citations) {
                if (citation >= h) { // h번 이상 인용된 논무이라면
                    count++;
                }
            }

            if (count >= h && citations.length - count <= h) {
                hIndex = Math.max(hIndex, h);
            }
        }

        return hIndex;
    }
}