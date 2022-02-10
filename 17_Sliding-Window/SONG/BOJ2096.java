import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2096 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int N = Integer.parseInt(br.readLine());
        int[] max = new int[3];
        int[] min = new int[3];

        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int n0 = Integer.parseInt(st.nextToken());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());

            if(i==0) {
                max[0] = min[0] = n0;
                max[1] = min[1] = n1;
                max[2] = min[2] = n2;
            } else {
                int max1 = max[1];
                max[1] = Math.max(Math.max(max[0], max[1]), max[2]) + n1; // 셋 중에 큰걸로 가져옴
                max[0] = Math.max(max[0], max1) + n0; // 0이랑 1에서만 올 수 있음
                max[2] = Math.max(max[2], max1) + n2;

                int min1 = min[1];
                min[1] = Math.min(Math.min(min[0], min[1]), min[2]) + n1; // 셋 중에 큰걸로 가져옴
                min[0] = Math.min(min[0], min1) + n0; // 0이랑 1에서만 올 수 있음
                min[2] = Math.min(min[2], min1) + n2;
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(Math.max(Math.max(max[0], max[1]), max[2]) + " ");
        sb.append(Math.min(Math.min(min[0], min[1]), min[2]));
        System.out.println(sb.toString());
    }
}
