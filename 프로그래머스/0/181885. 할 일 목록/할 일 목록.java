import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        List<String> result = new ArrayList<String>();
        
        for (int i = 0; i < finished.length; i++) {
            if (!finished[i]) {
                result.add(todo_list[i]);
            }
        }
        
        String[] answer = result.toArray(new String[0]);
        return answer;
    }
}