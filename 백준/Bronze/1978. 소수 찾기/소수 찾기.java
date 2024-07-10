

import java.util.Scanner;

public class Main {
    private static boolean validPrimeNumber(int num) {
        if (num == 1) {
            return false;
        }

        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count = 0;

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            if (validPrimeNumber(num)) {
                count++;
            }
        }

        System.out.println(count);
    }
}
