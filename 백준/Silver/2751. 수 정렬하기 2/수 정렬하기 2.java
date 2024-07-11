//package baekjoon;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Integer> li = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            li.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(li); // Arrays.sort() 과 다른 정렬 알고리즘 사용

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int e : li) {
            bw.write(e +"\n");
        }
        bw.flush();
    }
}
