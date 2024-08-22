// package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 집합 S에 있는 문자열
        int m = Integer.parseInt(st.nextToken()); // 검사해볼 문자열

        Set<String> s = new HashSet<>();
        for (int i = 0; i < n; i++) {
            s.add(br.readLine());
        }

        int count = 0;
        for (int i = 0; i < m; i++) {
            String queryString = br.readLine();
            if (s.contains(queryString)) {
                count++;
            }
        }

        System.out.println(count);
    }
}
