package geometry;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2166 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[][] point = new long[N+1][2];
        for(int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            point[i][0] = Long.parseLong(st.nextToken()); //x
            point[i][1] = Long.parseLong(st.nextToken()); //y
        }
        point[N] = point[0].clone(); //마지막이랑 처음이랑 곱해야하므로
        
        long a = 0;
        long b = 0;

        for(int i=0; i<N; i++) {
            a += point[i][0] * point[i+1][1];
            b += point[i][1] * point[i+1][0];
        }
        System.out.println(String.format("%.1f", Math.abs(a - b)/2D));
    }
}
