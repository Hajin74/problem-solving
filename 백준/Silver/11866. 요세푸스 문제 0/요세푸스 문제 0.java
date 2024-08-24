// package baekjoon;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int k = scanner.nextInt();

        // 원형 테이블 만들기
        List<Integer> table = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            table.add(i);
        }

        // 요세푸스 순열로 제거하기
        List<Integer> removedOrder = new ArrayList<>();
        int currentIndex = 0;
        while (table.size() > 0) {
            int nextIndex = currentIndex + k - 1;

            while (nextIndex > table.size() - 1) {
                int temp = nextIndex - table.size();
                nextIndex = temp;
            }

            removedOrder.add(table.get(nextIndex));
            table.remove(nextIndex);
            currentIndex = nextIndex;
        }

        // 출력
        String result = removedOrder.stream()
                .map(String::valueOf)
                .collect(Collectors.joining(", ", "<", ">"));
        System.out.println(result);
    }
}
