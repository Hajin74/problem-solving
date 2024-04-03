import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(br.readLine());

        for (int i = 0; i < count; i++) {
            String ex = br.readLine();
            if (isVPS(ex)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }

    public static boolean isVPS(String ex) {
        Stack<String> stack = new Stack<>();

        try {
            for (int i = 0; i < ex.length(); i++) {
                if (ex.charAt(i) == '(') {
                    stack.push("(");
                } else if (ex.charAt(i) == ')') {
                    stack.pop();
                }
            }

            return stack.isEmpty();
        } catch (Exception e){
            return false;
        }
    }
}