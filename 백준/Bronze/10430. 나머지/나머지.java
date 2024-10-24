import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int operation1 = (a+b)%c;
        int operation2 = ((a%c) + (b%c))%c;
        int operation3 = (a*b)%c;
        int operation4 = ((a%c) * (b%c))%c;

        System.out.println(operation1);
        System.out.println(operation2);
        System.out.println(operation3);
        System.out.println(operation4);
    }
}