// package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Set<String> neverHeardSet = new HashSet<>();
        for (int i = 0; i < n; i++) {
            neverHeardSet.add(br.readLine());
        }

        Set<String> neverSeenAndHeardSet = new TreeSet<>();
        for (int i = 0; i < m; i++) {
            String person = br.readLine();
            if (neverHeardSet.contains(person)) {
                neverSeenAndHeardSet.add(person);
            }
        }

        System.out.println(neverSeenAndHeardSet.size());
        for (String person : neverSeenAndHeardSet) {
            System.out.println(person);
        }
    }
}
