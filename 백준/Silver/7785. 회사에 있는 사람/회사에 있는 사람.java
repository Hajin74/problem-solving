// package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        HashSet<String> log = new HashSet<>();

        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            String name = input[0];
            String action = input[1];

            if (action.equals("enter")) {
                log.add(name);
            } else {
                log.remove(name);
            }
        }

        TreeSet<String> reverseLog = new TreeSet<>(Collections.reverseOrder());
        reverseLog.addAll(log);

        for (String name : reverseLog) {
            System.out.println(name);
        }
    }
}
