// package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int aNum = Integer.parseInt(input[0]);
        int bNum = Integer.parseInt(input[1]);

        HashSet<Integer> aSet = new HashSet<>();
        String[] a = br.readLine().split(" ");
        for (int i = 0; i < aNum; i++) {
            aSet.add(Integer.parseInt(a[i]));
        }

        HashSet<Integer> bSet = new HashSet<>();
        String[] b = br.readLine().split(" ");
        for (int i = 0; i < bNum; i++) {
            bSet.add(Integer.parseInt(b[i]));
        }

        // 대칭차집합 = a + b - 교집합
        int symmetricDifferenceNum = aSet.size() + bSet.size();

        // 교집합 개수 구하기
        aSet.retainAll(bSet);
        int intersectionNum = aSet.size();

        symmetricDifferenceNum = symmetricDifferenceNum - intersectionNum * 2;

        System.out.println(symmetricDifferenceNum);
    }
}
