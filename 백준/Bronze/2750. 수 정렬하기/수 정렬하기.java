//package baekjoon;

import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] li = new int[n];

        for (int i = 0; i < n; i++) {
            int e = sc.nextInt();
            li[i] = e;
        }

        Arrays.sort(li);

        for (int e : li) {
            System.out.println(e);
        }
    }
}
