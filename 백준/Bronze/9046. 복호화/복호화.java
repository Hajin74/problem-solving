// package 문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        String str = "";
        for (int h = 0; h < n; h++) {
            str = br.readLine().replace(" ", "");

            int[] arr = new int[26];
            for (int i = 0; i < str.length(); i++) {
                arr[str.charAt(i) - 'a']++;
            }

            int max = 0;
            int count = 0;
            char c = 'a';
            for (int j = 0; j < 26; j++) {
                if (arr[j] > max) {
                    max = arr[j];
                    count = 0;
                    c = (char)('a' + j);
                } else if (arr[j] == max) {
                    count++;
                }
            }

            if (count > 0) {
                System.out.println('?');
            } else {
                System.out.println(c);
            }
        }
    }
}
