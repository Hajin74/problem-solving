//package baekjoon;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(getGCD(a, b));
        System.out.println(getLCD(a, b));

        sc.close();
    }

    // 최대공약수 : a % b = r 일 때, a와 b의 최대공약수와 b와 r의 최대공약수는 같다
    public static int getGCD(int a, int b) {
        if (a < b) {
            int temp = a;
            a = b;
            b = temp;
        }

        if (a % b == 0){
            return b;
        }

        // 반복문 방식
//        while (true) {
//            int r = a % b;
//            if (r == 0) {
//                return b;
//            }
//            a = b;
//            b = r;
//        }

        return getGCD(b, a % b);
    }

    // 최소공배수 : a * b % 최대공약수
    public static int getLCD(int a, int b) {
        int gcd = getGCD(a, b);
        return a * b / gcd;
    }
}
