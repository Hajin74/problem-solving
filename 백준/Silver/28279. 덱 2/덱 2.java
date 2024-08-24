// package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Deque<Integer> deq = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int order = Integer.parseInt(st.nextToken());

            switch (order) {
                case 1 :
                    deq.addFirst(Integer.parseInt(st.nextToken()));
                    break;
                case 2:
                    deq.addLast(Integer.parseInt(st.nextToken()));
                    break;
                case 3:
                    if (!deq.isEmpty()) {
                        System.out.println(deq.removeFirst());
                    } else {
                        System.out.println(-1);
                    }
                    break;
                case 4:
                    if (!deq.isEmpty()) {
                        System.out.println(deq.removeLast());
                    } else {
                        System.out.println(-1);
                    }
                    break;
                case 5:
                    System.out.println(deq.size());
                    break;
                case 6:
                    if (deq.isEmpty()) {
                        System.out.println(1);
                    } else {
                        System.out.println(0);
                    }
                    break;
                case 7:
                    if (!deq.isEmpty()) {
                        System.out.println(deq.peekFirst());
                    } else {
                        System.out.println(-1);
                    }
                    break;
                case 8:
                    if (!deq.isEmpty()) {
                        System.out.println(deq.peekLast());
                    } else {
                        System.out.println(-1);
                    }
                    break;
            }
        }
    }
}
