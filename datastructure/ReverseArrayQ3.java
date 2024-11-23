package datastructure;

public class ReverseArrayQ3 {
    public static void main(String[] args) {
        int[] arr = new int[]{5, 10, 73, 2, -5, 42};

        int sum = sumOf(arr);
        System.out.println("sum: " + sum);
    }

    static int sumOf(int[] a) {
        int sum = 0;
        for (int i = 0; i < a.length; i++) {
            sum += a[i];
        }
        return sum;
    }
}
