package datastructure;

import java.util.Arrays;

public class ReverseArrayQ2 {
    public static void main(String[] args) {
        int[] arr = new int[]{5, 10, 73, 2, -5, 42};

        reverse(arr);
    }

    static void reverse(int[] arr) {
        for (int i = 0; i < arr.length / 2; i++) {
            System.out.println(Arrays.toString(arr));
            System.out.println(i + "번째와 " + (arr.length - i - 1) + "번째를 교환합니다.");

            swap(arr, i, arr.length - i - 1);
        }

        System.out.println(Arrays.toString(arr));
        System.out.println("역순 정렬을 마쳤습니다.");
    }

    static void swap(int[] arr, int index1, int index2) {
        int temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }
}
