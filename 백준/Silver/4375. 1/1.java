/**
 * 모듈러 (나머지 연산)
 * a % b = c 와 (a % c + b % c) % c 는 같다.
 * 나머지의 자료형이 커질 때 사용하기 좋다.
 */


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            System.out.println(getSmallestOnlyOneNumber(n));
        }

        sc.close();
    }

    public static int getSmallestOnlyOneNumber(int num) {
        long result = 0;
        int count = 0;

        while (true) {
            result = (result * 10 + 1) % num;
            count++;
            if (result % num == 0) {
                return count;
            }
        }
    }
}
