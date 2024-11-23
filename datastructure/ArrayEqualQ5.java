package datastructure;

import java.util.Arrays;
import java.util.Scanner;

public class ArrayEqualQ5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int num = scanner.nextInt();
        int[] a = new int[num];
        int[] b = new int[num];
        
        for (int i = 0; i < num; i++) {
            b[i] = scanner.nextInt();
        }

        rcopy(a, b);

        System.out.println(Arrays.toString(a));
        System.out.println(Arrays.toString(b));
    }

    static void rcopy(int[] a , int[] b) {
        for (int i = 0; i < a.length; i++) {
            a[a.length - i - 1] = b[i];
        }
    }
}
