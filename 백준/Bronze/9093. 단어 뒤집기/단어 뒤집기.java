import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());

        while (n > 0) {
            String[] words = bf.readLine().split(" ");
            for (String word : words) {
                StringBuilder sb = new StringBuilder(word);
                System.out.print(sb.reverse() + " ");
            }
            System.out.println();

            n--;
        }
        
        bf.close();
    }
}
