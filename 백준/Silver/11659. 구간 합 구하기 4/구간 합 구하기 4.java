import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());

        int[] s = new int[n + 1];
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        for (int i = 1; i <= n; i++) {
            s[i] = s[i-1] + Integer.parseInt(stringTokenizer.nextToken());
//            System.out.println(s[i]);
        }

        for (int i = 0; i < m; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int start = Integer.parseInt(stringTokenizer.nextToken());
            int end = Integer.parseInt(stringTokenizer.nextToken());

            System.out.println(s[end] - s[start - 1]);
        }


    }
}
