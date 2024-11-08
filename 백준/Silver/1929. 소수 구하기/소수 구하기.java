/**
 * 소수 구하기
 * 제곱근까지만 탐색해도 된다 -> bc 약수의 대칭성
 */


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();

        for (int i = m; i <= n; i++) {
            if (getPrimeNumber(i)) {
                System.out.println(i);
            }
        }
    }

    public static boolean getPrimeNumber(int num) {
        if (num == 1) {
            return false;
        }
        
        for (int i = 2; i <= Math.pow(num, 0.5); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
