package datastructure;

import java.util.Scanner;
import java.util.Arrays;

public class ArrayEqualQ4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int num = scanner.nextInt();
        int[] a = new int[num];
        int[] b = new int[num];
        
        for (int i = 0; i < num; i++) {
            b[i] = scanner.nextInt();
        }

        copy(a, b);

        System.out.println(Arrays.toString(a));
        System.out.println(Arrays.toString(b));
    }

    static void copy(int[] a , int[] b) {
        for (int i = 0; i < a.length; i++) {
            a[i] = b[i];
        }
    }
}
