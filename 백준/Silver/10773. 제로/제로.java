

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(reader.readLine());

        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < k; i++) {
            list.add(Integer.parseInt(reader.readLine()));
        }

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < k; i++) {
            if (list.get(i) != 0) {
                stack.push(list.get(i));
            } else {
                stack.pop();
            }
        }

        List<Integer> result = new ArrayList<>(stack);
        System.out.println(result.stream().mapToInt(Integer::intValue).sum());

    }
}
