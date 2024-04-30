// package 누적합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st1 = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st1.nextToken());
        int m = Integer.parseInt(st1.nextToken());

        int[][] arr = new int[n][m];
        for (int i = 0; i < n; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st2.nextToken());
            }
        }

//        System.out.println(Arrays.deepToString(arr));

        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            StringTokenizer st3 = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st3.nextToken());
            int b = Integer.parseInt(st3.nextToken());
            int x = Integer.parseInt(st3.nextToken());
            int y = Integer.parseInt(st3.nextToken());

            int sum = 0;
            for (int q = a - 1; q <= x - 1; q++) {
                for (int w = b - 1; w <= y - 1; w++) {
//                    System.out.println(arr[q][w]);
                    sum += arr[q][w];
                }
            }

            System.out.println(sum);
        }

    }
}
