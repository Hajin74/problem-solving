import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static int n;
    static int m;
    static int[] input;
    static int[] result;
    static boolean[] visited;

    private static void dfs(int level) {
        if (level == m) {
            printArr(result);
        }
        else {
            for (int i = 0; i < n; i++) {
                if (!visited[i]) {
                    result[level] = input[i];
                    visited[i] = true;

                    dfs(level + 1);

                    visited[i] = false;
                }
            }
        }
    }

    private static void printArr(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // 입력받기 & 할당
        n = sc.nextInt();
        m = sc.nextInt();

        input = new int[n];
        for (int i = 1; i <= n; i++) {
            input[i-1] = i;
        }

        result = new int[m];
        visited = new boolean[n];

        // 순열
        dfs(0);

        sc.close();
    }
}
