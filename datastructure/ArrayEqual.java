package datastructure;

import java.util.Scanner;

public class ArrayEqual {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int na = scanner.nextInt();
        int[] arrA = new int[na];
        for (int i = 0; i < na; i++) {
            arrA[i] = scanner.nextInt();
        }

        int nb = scanner.nextInt();
        int[] arrB = new int[nb];
        for (int i = 0; i < nb; i++) {
            arrB[i] = scanner.nextInt();
        }

        System.out.println(equals(arrA, arrB) ? "같은 배열입니다" : "다른 배열 입니다.");
    }

    static boolean equals(int[] a, int[] b) {
        if (a.length != b.length) {
            return false;
        }

        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }

        return true;
    }
}
