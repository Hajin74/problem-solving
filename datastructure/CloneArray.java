package datastructure;

public class CloneArray {
    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5};
        int[] b = a.clone();

        b[3] = 0;

        for (int i = 0; i < a.length; i++) {
            System.out.print(" " + a[i]);
        }
        System.out.println();

        for (int i = 0; i < b.length; i++) {
            System.out.print(" " + b[i]);
        }

    }
}
